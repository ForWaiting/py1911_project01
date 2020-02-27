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


class GoodSerializer1(serializers.ModelSerializer):

    # 在序列化时指定字段 《在多方》使用source = 模型名.字段名
    # read_only 表示只读不能更改(get显示，update不显示)
    # write_only 表示只读不能更改(get不显示，update显示)
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('id','name','desc','category')
class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """
    def to_representation(self, value):
        """

        :param value: 需要序列化的对象
        :return: 显示的格式
        """
        return str(value.id)+'--'+value.name+'--'+value.desc

class CategorySerializer(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=2,error_messages={
        'max_length':'最多10个中文字符',
        'min_length':'最少2个中文字符',
    })

    def create(self, validated_data):
        """
        通过重写create方法来创建模型方式
        :param validated_data:
        :return:
        """
        instance = Category.objects.create(**validated_data)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例子
        """
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class CategorySerializer1(serializers.ModelSerializer):
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
    # 使用自定义序列化类
    # goods = CustomSerializer(many=True,read_only=True)
    # goods = GoodSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('id','name','goods')


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        'max_length': '最大20个中文字符',
        'min_length': '最小2个字符'
    })
    category = CategorySerializer(label='分类')

    def validate_category(self,category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回新值
        """
        try:
            Category.objects.get(name = category['name'])
        except:
            raise serializers.ValidationError('输入的分类名不存在')
        return category

    def validate(self, attrs):
        try:
            c = Category.objects.get(name=attrs['category']['name'])
        except:
            c = Category.objects.create(name = attrs['category']['name'])
        attrs['category'] = c
        return attrs

    def create(self, validated_data):
        instance = Good.objects.create(**validated_data)
        instance.save()
        return instance