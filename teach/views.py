from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

from datetime import datetime


def hello(request):
    return HttpResponse("hello !we in <b>%s</b> page" % request.path)


def hello2(request):
    now = datetime.now()
    html = '<b>time now is -</b> %s' % now
    return HttpResponse(html)


def hello3(request, param='Default'):
    html = '<b>param in url string -</b> %s' % param
    return HttpResponse(html)


def hello4(request):
    now = datetime.now()
    t = get_template('hello/hello4.html')
    html = t.render({'date': now})
    return HttpResponse(html)


def hello5(request):
    now = datetime.now()
    return render_to_response('hello/hello4.html', {
        'date': now,
        'path': request.path
    })


def hello6(request):
    return render_to_response('hello/djinfo.html', {
        'meta': request.META,
        'meta_k': request.META.keys(),
        'meta_v': request.META.values(),
        'path': request.path
    })
