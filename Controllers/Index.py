# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from Models.ArticlesModel import articles, add


def index(request):
    lists   = articles()
    output  = []
    for k, v in enumerate(lists):
        temp_dic = {
            'id'    : str(v._id),
            'title' : v.title,
            'create': v.create
        }
        output.append(temp_dic)

    context = {}
    context['list'] = output
    return render(request, 'index/index.html', context)

def create(request):

    id = add(request)

    context = {}
    context['id'] = id
    return render(request, 'index/index.html', context)