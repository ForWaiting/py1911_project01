# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2020/3/16 17:50
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from flask import render_template,Blueprint
from models.book import *

bookbp = Blueprint('books',__name__)

@bookbp.route('/')
def index():

    cs = Category.query.all()
    return render_template('index.html', cs=cs)

@bookbp.route('/categorys/<id>')
def category(id):
    c = Category.query.filter_by(id=id).first()
    if c:
        # 表关联查询
        # bs = Book.query.filter_by(cid=id).all()
        # 关系字段查询
        bs = c.books
        # print(bs[0].category)
        return render_template('category.html',bs=bs)
    return '书籍不存在'