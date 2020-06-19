# -*- encoding: utf-8 -*-
"""
@File    : myfun.py
@Time    : 2020/2/21 9:09
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django.template import Library
from ..models import Article, Category, Tag

register = Library()


# 自定义过滤器
@register.filter
def date_format(data):
    return "%d-%d-%d" % (data.year, data.month, data.day)


@register.filter
def author_format(author, info):
    return info + ':' + author.upper()


@register.simple_tag
def get_latest_articles(num = 3):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_latest_dates(num = 3):
    dates = Article.objects.dates('create_time','month','DESC')[:num]
    return dates

@register.simple_tag
def get_categorys():
    return Category.objects.all().order_by('-id')

@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by('-id')