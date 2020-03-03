# -*- encoding: utf-8 -*-
"""
@File    : permissions.py
@Time    : 2020/3/3 14:12
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
"""
可以自定义权限
"""
from rest_framework import permissions


class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class OrdersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
