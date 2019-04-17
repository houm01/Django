#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com
from django import forms
from django.core.validators import RegexValidator
from pye.models import Device


class DeviceForm(forms.Form):
    required_css_class = 'required'
    name = forms.CharField(max_length=50,
                           min_length=2,
                           label='设备名称',
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))

    ip_address = forms.GenericIPAddressField(label='IP地址',
                                             required=True,
                                             widget=forms.TextInput(attrs={"class": "form-control"}))

    ro_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='只读community',
                                   required=True,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    rw_community = forms.CharField(max_length=50,
                                   min_length=2,
                                   label='读写community',
                                   required=False,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))

    username = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH用户名',
                               required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(max_length=50,
                               min_length=2,
                               label='SSH密码',
                               required=False,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))

    enable_password = forms.CharField(max_length=50,
                                      min_length=2,
                                      label='enable密码',
                                      required=False,
                                      widget=forms.PasswordInput(attrs={"class": "form-control"}))

    device_type_choices = (('ASA','ASA'),('Router','Router'),('Switch','Switch'))
    device_type = forms.CharField(max_length=10,
                                  label='设备类型',
                                  widget=forms.Select(choices=device_type_choices,attrs={"class": "form-control"}))

    def clean_ip_address(self):
        ip_address = self.cleaned_data['ip_address']
        existing = Device.objects.filter(ip_address=ip_address).exists()

        if existing:
            raise forms.VaildationError("IP地址已存在")
        return ip_address

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        if not (password and username):
            raise forms.VaildationError('用户名和密码需要同时填写')
        return password







