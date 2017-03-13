"""teach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from teach.views import *
from books.views import *

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', hello),
# ]

urlpatterns = patterns('',
    (r'^admin/', admin.site.urls),
    (r'^hello/$', hello),
    (r'^hello2/$', hello2),

    (r'^hello3/(\d{1,2})/$', hello3),
    (r'^hello3/$', hello3),

    (r'^hello4/$', hello4),
    (r'^hello5/$', hello5),
    (r'^hello6/$', hello6),


    (r'^books/$', getbooks),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contactform/$', contactform),
    (r'^contact/thanks/$', thanks),

)