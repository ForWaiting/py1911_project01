# -*- encoding: utf-8 -*-
"""
@File    : filter_fun.py
@Time    : 2020/2/25 16:28
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from ..models import Category,SelfIntroduction
from django.template import Library
register = Library()

@register.simple_tag
def get_category():
    return Category.objects.all().order_by('id')

@register.simple_tag
def get_user():
    return SelfIntroduction.objects.first()