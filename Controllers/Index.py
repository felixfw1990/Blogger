# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from Models.ArticlesModel import list, add


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index/index.html', context)

def create(request):

    id = add(request)

    context = {}
    context['id'] = id
    return render(request, 'index/index.html', context)