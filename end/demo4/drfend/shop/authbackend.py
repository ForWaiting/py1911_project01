# -*- encoding: utf-8 -*-
"""
@File    : authbackend.py
@Time    : 2020/3/4 10:35
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
"""
实现自定义认证类（登录 内容）
"""
from django.contrib.auth import backends
from shop.models import User
from django.db.models import Q
class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        """

        :param request:
        :param kwargs:认证参数
        :return: 如果认证成功返回认证参数，否贼返回None
        """
        username = kwargs['username']
        password = kwargs['password']
        user = User.objects.filter(Q(username= username)|Q(email = username)|Q(telephone=username)).first()
        if user:
            if user.check_password(password):
                return user
            else:
                return None
        else:
            return None
