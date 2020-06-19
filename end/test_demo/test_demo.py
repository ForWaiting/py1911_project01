# -*- encoding: utf-8 -*-
"""
@File    : test_demo.py
@Time    : 2020/3/20 9:41
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return '这里是Nginx+Gunicon部署项目'

if __name__ == '__main__':
    app.run()
