from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE 等HTTP动作
    queryset 指明 需要操作的模型表

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImg.objects.all()
    serializer_class = GoodImgsSerializer
