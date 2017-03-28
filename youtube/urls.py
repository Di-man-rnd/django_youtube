from django.conf.urls import url, patterns, include
from django.contrib import admin
from teach.views import *
from books.views import *
from youtube.views import *


urlpatterns = [
    url(r'^$', all_bloger, name='all+bloger'),
    url(r'^setcat/$', set_cat),
    url(r'^([0-9]+)/$', detail_bloger, name='detail_bloger'),
]

