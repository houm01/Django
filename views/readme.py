#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com


from django.shortcuts import render
from datetime import datetime
from data import courses_db


def readme(request):
    mytime = int(datetime.now().strftime("%w"))
    network_python = '介绍'
    readme = 'readme_body'
    courses_list = ['安全','Python','DC']
    teacher_list = [{'courses':'安全','teacher':'现任明教教主'},
                    {'courses':'安全','teacher':'马老师'},
                    {'courses':'数据中心','teacher':'安德'},
                    {'courses':'教主VIP','teacher':'现任明教教主'},]

    return render(request,'README.html',locals())  # locals() 表示把本地变量都传进去


def sec_course(request):
    return render(request,'course.html',{'courseinfo': courses_db.sec})


def dc_course(request):
    return render(request, 'course.html', {'courseinfo': courses_db.dc})



    # return render(request, 'README.html',{'network_python': '介绍',
    #                                       'readme': 'readme_body',
    #                                       'courses_list': courses_list,
    #                                       'teacher_list': teacher_list,
    #                                       'mytime': mytime},
    #               )