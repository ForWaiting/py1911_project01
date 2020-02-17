# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/2/17 17:40
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django.conf.urls import url
from django.http import FileResponse


def load(request,filename):
    return FileResponse(open(filename,"rb"),content_type="application/msword",filename=filename,
                        as_attachment=True)
app_name = 'dowmload'
urlpatterns = [
    url(r'^(.*?)/$',load)
]