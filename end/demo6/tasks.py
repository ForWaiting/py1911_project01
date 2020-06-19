# -*- encoding: utf-8 -*-
"""
@File    : tasks.py
@Time    : 2020/3/18 14:27
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""

# pip install celery安装 celery
# 安装Redis数据库
# pip install redis 安装python 处理redis数据库驱动

from factory import create_app
from celery import Celery
import time
from flask_mail import Message
from views import mail

# celery 操作由celery实例开始
app = Celery("tasks",broker="redis://127.0.0.1:6379/10",backend='redis://127.0.0.1:6379/11')

@app.task()
def send_email(email,serstr):
    print('开始发送')
    with create_app().app_context():
        msg = Message(subject='你好，激活账户点击下方', recipients=[email])
        msg.html = "<a href='http://127.0.0.1:5000/active/%s' >点击激活</a>" % (serstr,)
        mail.send(msg)
        print('发送完毕')

