#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com

from pye.models import Device
from django.shortcuts import render
from pye.houm01_forms import DeviceForm
from django.http import HttpResponseRedirect


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            s1 = Device(name=request.POST.get('name'),
                        ip_address=request.POST.get('ip_address'),
                        ro_community=request.POST.get('ro_community'),
                        rw_community=request.POST.get('rw_community'),
                        username=request.POST.get('username'),
                        password=request.POST.get('password'),
                        enable_password=request.POST.get('enable_password'),
                        device_type=request.POST.get('device_type'))

            s1.save()

            form = DeviceForm()
            return render(request,'add_device.html',{'form': form,
                                                     'successmessage': '设备添加成功'})

        else:
            return render(request,'add_device.html',{'form': form})
    else:
        form = DeviceForm()
        return render(request,'add_device.html',{'form': form})

