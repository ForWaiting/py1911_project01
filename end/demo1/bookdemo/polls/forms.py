# -*- encoding: utf-8 -*-
"""
@File    : forms.py
@Time    : 2020/2/19 9:44
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from django import forms
from .models import User
class LoginForm(forms.Form):
    """
    定义一个登录表单用于生成html 登录表单
    """
    username = forms.CharField(max_length=150,min_length=3,label='输入用户名',help_text='用户名最小3，最大150')
    password = forms.CharField(max_length=150,min_length=3,widget=forms.PasswordInput,help_text='密码最小3，最大150',label='输入密码')


class RegistForm(forms.ModelForm):
    """
    定义一个注册表单用于生成注册表单
    """
    password2 = forms.CharField(widget=forms.PasswordInput,label='重复密码')
    class Meta:
        model = User
        fields = ['username','password']
        labels = {'username':'用户名','password':"密码"}
        help_texts = {'username':'长度3-150','password':'长度3-150'}
        widgets = {'password':forms.PasswordInput}