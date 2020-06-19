# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/2/25 9:09
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django.conf.urls import url
from . import views
app_name = 'myblogapp'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^details/(\d+)/$',views.details,name='details'),
    url(r'^whisper/$',views.whisper,name='whisper'),
    url(r'^leacots/$',views.leacots,name='leacots'),
    url(r'^album/$',views.album,name='album'),
    url(r'^about/$',views.about,name='about'),
    url(r'^favicon.ico/$',views.favicon,name='favicon'),
]