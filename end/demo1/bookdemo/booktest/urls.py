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
    url(r'^detail/(\d+)',views.detail,name='detail')

]