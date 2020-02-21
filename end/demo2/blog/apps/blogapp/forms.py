# -*- encoding: utf-8 -*-
"""
@File    : forms.py
@Time    : 2020/2/21 17:05
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','url','email','body']
        labels = {
            'name':'名字：',
            'url':'网址：',
            'email':'邮箱：',
            'body':'评论：'
        }
        widgets = {
            'body':forms.Textarea()
        }