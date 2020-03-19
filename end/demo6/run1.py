# -*- encoding: utf-8 -*-
"""
@File    : run1.py
@Time    : 2020/3/16 9:44
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from factory import create_app
from models import *

# 3启动web服务
if __name__ == '__main__':
    # 开发环境使用 debug = True 自动重启服务器
    app = create_app()
    # db.drop_all()
    # db.create_all()
    create_app().run(host='127.0.0.1',port=5000,debug=True)

