"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

#路由  网址 每一个网址均需要绑定视图函数  视图函数给予页面返回
# 每一个路由都需要和视图函数绑定
# MVT V 视图函数 3个作用 接受请求 处理数据 返回相应

# def list(response):
#     return HttpResponse("这里是列表页面")
# def jsondata(response):
#     return HttpResponse("{'name':'Luffy','age':19}")
# def index(response):
#     return HttpResponse("这里是首页")

# 总的路由匹配文件
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('list/', list),
    # path('json/', jsondata),
    # path('index',index),
    # 使用path 将booktest 的路由进行包含
    path('booktest/', include('booktest.urls'))
]
