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
    # 视图函数FBV路由
    url(r'^$',views.poll_index,name='poll_index'),
    url(r'^polldetail/(\d+)$',views.poll_detail, name='poll_detail'),
    url(r'^pollresult/(\d+)$',views.poll_result, name='poll_result'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^logout/$',views.logout,name='logout')

    # 视图类CBV路由
    # url(r'^$', views.PollIndexView.as_view(), name='poll_index'),
    # url(r'^polldetail/(\d+)$', views.PollDetailView.as_view(), name='poll_detail'),
    # url(r'^pollresult/(\d+)$', views.PollResultView.as_view(), name='poll_result'),

]