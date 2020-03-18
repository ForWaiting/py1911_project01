# -*- encoding: utf-8 -*-
"""
@File    : run2.py
@Time    : 2020/3/18 14:42
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""

from tasks import dosomething

if __name__ == '__main__':
    # dosomething()
    # dosomething()
    # dosomething()

    dosomething.delay()
    dosomething.delay()
    dosomething.delay()
    print("所有任务完工了")