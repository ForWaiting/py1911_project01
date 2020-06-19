# -*- encoding: utf-8 -*-
"""
@File    : throttling.py
@Time    : 2020/3/4 14:23
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from rest_framework import throttling

class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon':'1000/day'
    }
class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user':'10000/day'
    }