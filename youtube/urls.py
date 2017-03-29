from django.conf.urls import url, patterns, include
from django.contrib import admin
from teach.views import *
from books.views import *
from youtube.views import *

# url:  /bloger/ =>
urlpatterns = [
    # Function
    url(r'^$', all_bloger, name='all_bloger'),
    url(r'^([0-9]+)/$', detail_bloger, name='detail_bloger'),

    # Class
    url(r'^list/$', BlogerList.as_view()),

    # js AJAX
    url(r'^setcat/$', set_cat),
]

