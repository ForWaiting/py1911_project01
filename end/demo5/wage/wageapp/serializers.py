# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2020/3/2 10:37
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=2,error_messages={
        'max_length':'最多10个中文字符',
        'min_length':'最少2个中文字符',
    })

    def create(self, validated_data):
        instance = Department.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=2, error_messages={
        'max_length': '最多10个中文字符',
        'min_length': '最少2个中文字符',
    })

    def validate_department(self, attrs):
        Department.objects.get(name=attrs['name'])
        return attrs
    def validate(self, attrs):
        department = Department.objects.get(name=attrs['department']['name'])
        attrs['department'] = department
        return attrs

    def create(self, validated_data):
        instance = Employee.objects.create(**validated_data)
        instance.save()
        return instance