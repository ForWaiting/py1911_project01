# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2020/3/16 17:50
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
import sqlite3
from flask import request, render_template, flash, redirect, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer,SignatureExpired,BadSignature
import time

userbp = Blueprint('user', __name__)


# 4绑定路由与试图函数，进行账户注册
@userbp.route('/login', methods=['GET', 'POST'])
def login():
    # 5 flask中请求的对象封装在request中 request代表请求
    # print('登录中的参数', request, request.method)
    if request.method == 'GET':
        # 7使用render_template渲染jinja2模板 模板文件夹和python模块同级目录
        # 8 静态资源static 用法同template ，render_template第二参数 为传入模板的数据
        flash({})
        category_list = [{'ID': 101, 'Name': '汽车'}, {'ID': 102, 'Name': '房产'}]
        user = [{'Name': 'Luffy'}]
        return render_template('login.html', cl=category_list, u=user)
    elif request.method == 'POST':
        # 6 从form中提取表单参数
        email = request.form.get('email')
        password = request.form.get('password')
        error = None
        if not email:
            error = '用户名必须填写'
        elif not password:
            error = '密码必须填写'

        # 9使用flash 可以将参数传入下一个请求，此处将error写入下一次请求，
        # 是将flash传入的参数写入session，前端提示信息从浏览器session中获取参数
        if error:
            flash({
                'error': error,
                'email': email,
                'password': password,
            })
            return redirect('/login')
        else:
            # 使用with 会自动关闭游标以及数据库
            with sqlite3.connect('demo6.db') as con:
                cur = con.cursor()
                cur.execute('select * from user where email = ?', (email,))
                r = cur.fetchall()
                if len(r) <= 0:
                    flash({
                        'error': '邮箱错误'
                    })
                    return redirect('/login')
                else:
                    security_password = r[0][2]
                    if not check_password_hash(security_password, password):
                        flash({
                            'error': '密码错误'
                        })
                        return redirect('/login')
                    else:
                        if r[0][5] == 0:
                            flash({
                                'error': '用户尚未激活'
                            })
                            return redirect('/login')
                        else:
                            return '登陆成功%s--%s' % (email, password)


# 进行账户注册
@userbp.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not email:
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
            # 查找数据库是否存在当前账户
            with sqlite3.connect('demo6.db') as con:
                cur = con.cursor()
                cur.execute('select * from user where email = ?', (email,))
                r = cur.fetchall()
                if len(r) > 0:
                    flash({
                        'error': '邮箱已存在'
                    })
                    return redirect('/regist')
                else:
                    # 进行账户注册
                    try:
                        security_password = generate_password_hash(password)
                        cur.execute('insert into user (email,password) values(?,?)', (email, security_password))
                        cur.execute('select id from user where email = ?', (email,))
                        user_id = cur.fetchone()[0]
                        from flask_mail import Message
                        from .utils import mail

                        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key,expires_in=24*60*60)
                        serstr = serUtil.dumps({'user_id':user_id}).decode('utf-8')

                        from tasks import send_email
                        send_email.delay(email,serstr)
                        # msg = Message(subject='你好，激活账户点击下方', recipients=[email])
                        # msg.html = "<a href='http://127.0.0.1:5000/active/%s' >点击激活</a>" % (serstr,)
                        # mail.send(msg)

                        con.commit()
                        return '成功注册,请前往邮箱激活账户'
                    except Exception as e:
                        print(e)
                        con.rollback()
                        return '出异常了'
# 对帐户进行查找激活
@userbp.route('/active/<user_id>')
def activeuser(user_id):
    try:
        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=24 * 60 * 60)
        user_id =  serUtil.loads(user_id)['user_id']

        with sqlite3.connect('demo6.db') as con:
            cur = con.cursor()
            cur.execute('update user set is_active=1 where id = ?', (user_id,))
            con.commit()
        return redirect('/login')
    except SignatureExpired:
        return '超时'
    except BadSignature:
        return '密钥错误'
    except Exception:
        return '未知原因错误'
