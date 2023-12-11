#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def zarir(request):
    return render(request, 'index.html', None)
