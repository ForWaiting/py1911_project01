# -*- encoding: utf-8 -*-
"""
@File    : pagination.py
@Time    : 2020/3/4 14:48
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""

from rest_framework import pagination

class MyPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'num'
