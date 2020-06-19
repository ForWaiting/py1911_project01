# -*- encoding: utf-8 -*-
"""
@File    : utils.py
@Time    : 2020/3/17 17:24
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
# 扩展flask
from flask import session,redirect,request
from flask_mail import Mail
from functools import wraps
mail = Mail()

def checklogin(f):
    @wraps(f)
    def check(*args,**kwargs):
        user = session.get('user')
        if user:
            return f(*args,**kwargs)
        else:
            return redirect('/login?next='+request.path)
    return check