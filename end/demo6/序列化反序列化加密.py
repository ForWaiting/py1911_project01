# -*- encoding: utf-8 -*-
"""
@File    : 序列化反序列化加密.py
@Time    : 2020/3/18 11:02
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from itsdangerous import TimedJSONWebSignatureSerializer,SignatureExpired,BadSignature
import time
id = 1001

seriaUtil = TimedJSONWebSignatureSerializer("hellopy1911",expires_in=3) # expries_in 加密有效期
serstr =  seriaUtil.dumps({"id":id}).decode("utf-8")
print("序列化结果",serstr)


try:
    seriaUtil = TimedJSONWebSignatureSerializer("hellopy1911")
    obj = seriaUtil.loads(serstr)
    print("反序列化对象", obj["id"])
except SignatureExpired as e:
    print(e,"过期了")
except BadSignature as e:
    print(e,"秘钥错误")