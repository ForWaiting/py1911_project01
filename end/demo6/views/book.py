# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2020/3/16 17:50
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from flask import render_template, flash,Blueprint


bookbp = Blueprint('books',__name__)

@bookbp.route('/')
def index():
    bookList = [{'ID': 101, 'Name': 'Luffy'}, {'ID': 102, 'Name': 'Nami'}, {'ID': 103, 'Name': 'Zoro'}]
    return render_template('index.html', bookList=bookList, u='hzf')