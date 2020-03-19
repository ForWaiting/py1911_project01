# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2020/3/19 10:34
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from .utils import db
from sqlalchemy import Column,ForeignKey
from sqlalchemy.orm import relationship,backref
class Category(db.Model):
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    name = db.Column('name',db.String(50),nullable=False,unique=True)

    def __repr__(self):
        return self.name

class Book(db.Model):
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    name = db.Column('name',db.String(50),nullable=False,unique=True)
    # 定义外键
    cid = db.Column('cid',db.ForeignKey('category.id'),nullable=False)
    # 定义关系字段
    category = db.relationship('Category',backref='books')

    def __repr__(self):
        return self.name