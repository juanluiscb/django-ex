# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

title = ":: Mundialito Rusia 2018"
titulo = ":: Mundialito Rusia 2018"
contexto = {
    'title': title,
    'titulo': titulo
}

def index(request):
    return render(request,'base.html',contexto)