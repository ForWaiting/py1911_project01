# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/2/20 9:26
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django.conf.urls import url
from . import views
app_name = 'blogapp'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^favicon.ico/$',views.favicon,name='favicon')

]