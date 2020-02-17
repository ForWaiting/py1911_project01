# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/2/16 15:49
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.poll_index,name='poll_index'),
    url(r'^polldetail/(\d+)$',views.poll_detail, name='poll_detail'),
    url(r'^pollresult/(\d+)$',views.poll_result, name='poll_result'),

]