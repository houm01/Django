#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
