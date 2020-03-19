# -*- encoding: utf-8 -*-
"""
@File    : admin.py
@Time    : 2020/3/19 15:42
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from flask import Blueprint, session, render_template, redirect, request
from .utils import checklogin
from models import *
adminbp = Blueprint('admin', __name__)


@adminbp.route('/admin')
@checklogin
def admin():
    """
    查看用户是否登录
    登陆了跳转admin页面，未登录去登录界面成功去admin
    :return:
    """
    # user = request.cookies.get('user')

    cs = Category.query.all()
    bs = Book.query.all()
    return render_template('admin/admin.html',cs=cs,bs=bs)


@adminbp.route('/admin/<resourcetype>/add',methods=['GET','POST'])
@checklogin
def add(resourcetype):
    if request.method == 'GET':
        resource = globals()[resourcetype.capitalize()]
        fields = []
        ps = dir(resource)
        for p in ps:
            if (not p.startswith('__')) and (not p.startswith('_')) and (p not in ['metadata','query','query_class','id','books','category']):
                fields.append(p)
        return render_template('admin/add.html',fs=fields)
    else:
        resource = globals()[resourcetype.capitalize()]
        r = resource()
        r.name = request.form['name']
        if isinstance(resource(),Book):
            r.cid = request.form['cid']
        db.session.add(r)
        db.session.commit()
        return redirect('/admin')

@adminbp.route('/admin/<resourcetype>/delete/<id>')
@checklogin
def delete(resourcetype,id):
    resource = globals()[resourcetype.capitalize()]
    r = resource.query.filter_by(id=id).first()
    db.session.delete(r)
    db.session.commit()
    return redirect('/admin')