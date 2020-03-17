# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2020/3/16 17:50
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from flask import  request, render_template, flash,redirect,Blueprint


userbp = Blueprint('user',__name__)

# 4绑定路由与试图函数
@userbp.route('/login', methods=['GET', 'POST'])
def login():
    # 5 flask中请求的对象封装在request中 request代表请求
    # print('登录中的参数', request, request.method)
    if request.method == 'GET':
        # 7使用render_template渲染jinja2模板 模板文件夹和python模块同级目录
        # 8 静态资源static 用法同template ，render_template第二参数 为传入模板的数据
        flash({})
        categoryList = [{'ID': 101, 'Name': '汽车'}, {'ID': 102, 'Name': '房产'}]
        user = [{'Name': 'Luffy'}]
        return render_template('login.html', cl=categoryList, u=user)
    elif request.method == 'POST':
        # 6 从form中提取表单参数
        username = request.form.get('username')
        password = request.form.get('password')
        error = None

        if not username:
            error = '用户名必须填写'
        elif not password:
            error = '密码必须填写'

        # 9使用flash 可以将参数传入下一个请求，此处将error写入下一次请求
        if error:
            flash({
                'error': error,
                'username': username,
                'password': password,
            })
            return redirect('/login')
        else:
            return '这里是提取参数页面%s--%s' % (username, password)


@userbp.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not username:
            error = "用户名不能为空"
        elif not password:
            error = "密码不能为空"
        elif not password2:
            error = "重复密码不能为空"
        elif password != password2:
            error = '密码不一致'
        if error:
            flash(error)
            return redirect('/regist')
        else:
            return '成功注册'
