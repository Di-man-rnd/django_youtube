from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect

import datetime

from teach.settings import BASE_DIR


def hello(request):
    return HttpResponse("hello !we in <b>%s</b> page" % request.path)


def hello2(request):
    now = datetime.datetime.now()
    html = '<b>time now is -</b> %s' % now
    return HttpResponse(html)


def hello3(request, param='Default'):
    html = '<b>param in url string -</b> %s' % param
    return HttpResponse(html)


def hello4(request):
    now = datetime.datetime.now()
    t = get_template('hello/hello4.html')
    html = t.render({'date': now})
    return HttpResponse(html)


def hello5(request):
    now = datetime.datetime.now()
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


def hello7(request, y, m, d):
    date2 = datetime.date(int(y), int(m), int(d))
    return HttpResponse(date2)


def hello7main(request):
    return HttpResponse('input  /hello7/YYYY/MM/DD/')


def home(request):
    return redirect('/contactform/')


def my_image(request):
    image_data = open(BASE_DIR+'/1.jpg', 'rb').read()
    return HttpResponse(image_data, mimetype='image/png')


def get_cookie(request):
    if 'color' in request.COOKIES:
        return HttpResponse('Ваш любимый цвет %s' % request.COOKIES['color'])
    else:
        return HttpResponse('У вас нет любимого цвета.')


def set_cookie(request):
    if 'color' in request.GET:
        response = HttpResponse('Ваш цвет : %s' % request.GET['color'])
        response.set_cookie('color', request.GET['color'])
        return response
    else:
        return HttpResponse('Вы не указали любимый цвет.')