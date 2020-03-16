# -*- encoding: utf-8 -*-
"""
@File    : generate_secret_key.py
@Time    : 2020/3/16 14:43
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
import os
secret_key = os.urandom(24)

print(secret_key)