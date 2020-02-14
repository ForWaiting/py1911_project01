# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/2/13 14:35
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
#引入路由绑定函数
from django.conf.urls import url
from . import views
#每个路由文件中必写路由数组
app_name = 'booktest'
urlpatterns = [
    # url(r'^index/$',views.index),
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    # 使用正则分组传递参数
    url(r'^detail/(\d+)$',views.detail,name='detail'),

    url(r'^deletebook/(\d+)$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)$',views.edithero,name='edithero'),
    url(r'^addbook/$',views.addbook,name='addbook'),

]