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
from django.conf import settings
from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from teach.views import *
from books.views import *

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', hello),
# ]

urlpatterns = patterns('',
    (r'^admin/youtube/bloger/(.*)/change/files/media/bloger/(.*)/change/$', get_img),
    (r'^admin/', admin.site.urls),
    (r'^hello/$', hello),
    (r'^hello2/$', hello2),

    (r'^hello3/(\d{1,2})/$', hello3),
    (r'^hello3/$', hello3),

    (r'^hello4/$', hello4),
    (r'^hello5/$', hello5),
    (r'^hello6/$', hello6),
    (r'^hello7/(?P<y>\d{4})/(?P<m>\d{2})/(?P<d>\d{2})/$', hello7),
    (r'^hello7/$', hello7main),


    (r'^books/$', getbooks),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contactform/$', 'books.views.contactform'), # === (r'^contactform/$', contactform, {dictionary: val})
    (r'^contact/thanks/$', thanks),
    (r'^$', home),
    (r'^img/$', my_image),
    (r'^get_cookie/$', get_cookie),
    (r'^set_cookie/$', set_cookie),

    (r'^books_v/$', IndexView.as_view()),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('',
        # (r'^debuginfo/$', debug),
    )