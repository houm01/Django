#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com


from django.shortcuts import render
from datetime import datetime
from data import courses_db
from houm01_demo.models import Courses
import json


def readme(request):
    mytime = int(datetime.now().strftime("%w"))
    network_python = '介绍'
    readme = 'readme_body'
    # courses_list = ['安全','Python','DC']
    courses_list = []
    teacher_list = []
    courses_result = Courses.objects.all()
    for x in courses_result:
        courses_list.append(x.courses_name)
        teacher_list.append({'courses':x.courses_name,'teacher': x.courses_teacher})



    # teacher_list = [{'courses':'安全','teacher':'现任明教教主'},
    #                 {'courses':'安全','teacher':'马老师'},
    #                 {'courses':'数据中心','teacher':'安德'},
    #                 {'courses':'教主VIP','teacher':'现任明教教主'},]

    return render(request,'README.html',locals())  # locals() 表示把本地变量都传进去


def sec_course(request):
    c = Courses.objects.get(courses_name='安全')
    courses_sec = {'方向': c.courses_name,
                   '摘要': c.courses_summary,
                   '授课老师': c.courses_teacher,
                   '授课方式': c.courses_method,
                   '课程特色': c.courses_characteristic,
                   '实验环境': c.courses_provide_lab,}
                   # '具体课程': json.loads(c.courses_detail)}
    return render(request,'course.html',{'courseinfo': courses_sec})


def dc_course(request):
    c = Courses.objects.get(courses_name='数据中心')
    courses_dc = {'方向': c.courses_name,
                   '摘要': c.courses_summary,
                   '授课老师': c.courses_teacher,
                   '授课方式': c.courses_method,
                   '课程特色': c.courses_characteristic,
                   '实验环境': c.courses_provide_lab,
                  }
                   # '具体课程': json.loads(c.courses_detail)}
    return render(request, 'course.html', {'courseinfo': courses_dc})



