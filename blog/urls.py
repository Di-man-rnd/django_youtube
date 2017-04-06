from django.conf.urls import url, patterns, include

from .views import *
from youtube.views import *


urlpatterns = [

    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^list/$', ListPage.as_view(), name='list'),
    url(r'^list/(.*)/$', ListPage.as_view(), name='category'),
    url(r'^detail/(?P<pk>[0-9]+)/$', DetailPage.as_view(), name='detail'),



    # url(r'^([0-9]+)/$', detail_bloger, name='detail_bloger'),
    # url(r'^(?P<pk>.*)/detail/$', BlogerDetail.as_view(), name='bloger_detail'), # pk or a slug.

]

