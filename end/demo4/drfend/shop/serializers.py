# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2020/2/26 15:41
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    指明 Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在 Meta 类中
    """
    #  goods 一定和 relate_name 一致
    # StringRelatedField() 可以显示关联模型中的__str__返回 // many=True 代表多了对象
    goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('name','goods')
class GoodSerializer(serializers.ModelSerializer):

    # 在序列化时指定字段 《在多方》使用source = 模型名.字段名 read_only 表示只读不能更改
    category_super = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name','desc','category_super')