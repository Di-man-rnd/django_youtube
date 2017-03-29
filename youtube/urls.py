from django.conf.urls import url, patterns, include
from django.contrib import admin
from teach.views import *
from books.views import *
from youtube.views import *

# url:  /bloger/ =>
urlpatterns = [
    url(r'^$', all_bloger, name='all_bloger'),
    url(r'^([0-9]+)/$', detail_bloger, name='detail_bloger'),

# js AJAX
    url(r'^setcat/$', set_cat),
]

