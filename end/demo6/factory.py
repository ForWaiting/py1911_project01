# -*- encoding: utf-8 -*-
"""
@File    : factory.py
@Time    : 2020/3/16 18:02
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
# flask 应用工厂
# 1引入Flask
from flask import Flask, render_template
from views import *

def create__app():
    # 2构建Flask对象  一个WSGI应用  __name__ 为Flask寻找static以及templates 提供支持
    app = Flask(__name__)
    # 10 session 是存储在服务器上的加密信息 会将sessionid保存在cookie
    app.secret_key = '\xc69\xa6\xfe\xbf0\xc8\x08\xb6\xe8y1\xde6\xb1\x91]\xe4G\x814\x93\xa7|'

    # 注册蓝图
    app.register_blueprint(bookbp)
    app.register_blueprint(userbp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    @app.add_template_filter
    def myupperfun(value):
        return value.capitalize()

    return app
