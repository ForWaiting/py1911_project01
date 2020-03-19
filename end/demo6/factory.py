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
from models import *
def create_app():
    # 2构建Flask对象  一个WSGI应用  __name__ 为Flask寻找static以及templates 提供支持
    app = Flask(__name__)
    # 10 session 是存储在服务器上的加密信息 会将sessionid保存在cookie
    app.secret_key = '\xc69\xa6\xfe\xbf0\xc8\x08\xb6\xe8y1\xde6\xb1\x91]\xe4G\x814\x93\xa7|'

    # 注册蓝图
    app.register_blueprint(bookbp)
    app.register_blueprint(userbp)


    # @app.before_first_request
    # def first_request_d0_something():
    #     import sqlite3
    #     try:
    #         con = sqlite3.connect('demo6.db')
    #         cur = con.cursor()
    #         cur.execute('DROP TABLE IF EXISTS user;')
    #         cur.execute("CREATE TABLE user (  id INTEGER PRIMARY KEY AUTOINCREMENT,  username TEXT UNIQUE NOT NULL,  password TEXT NOT NULL, create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 1 )")
    #         con.commit()
    #         cur.close()
    #         con.close()
    #     except Exception as e:
    #         print(e)

    # 404页面
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    @app.add_template_filter
    def myupperfun(value):
        return value.capitalize()

    # app.config["MAIL_SERVER"] = "smtp.163.com"
    # app.config["MAIL_PORT"] = 25
    # app.config["MAIL_USERNAME"] = "huangzhenfang2019@163.com"
    # app.config["MAIL_PASSWORD"] = "MIJLSURZTEZLGPAK"
    # app.config['MAIL_DEFAULT_SENDER'] = '草帽海贼团<huangzhenfang2019@163.com>'

    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25
    app.config["MAIL_USERNAME"] = "huangzhenfang2019@163.com"
    app.config["MAIL_PASSWORD"] = "MIJLSURZTEZLGPAK"
    app.config['MAIL_DEFAULT_SENDER'] = '路飞<huangzhenfang2019@163.com>'
    # 设置邮箱实例
    mail.init_app(app)

    # 配置数据库
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo6.db'
    # 自动检测更新
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.app =app
    return app
