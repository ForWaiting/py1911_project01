"""drfend URL Configuration

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
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from drfend.settings import MEDIA_ROOT
from shop.views import *
# 引入DRF自带的路由类
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
# 可以通过router 默认路由注册资源
router.register('categorys',CategoryViewSets)
router.register('goods',GoodViewSets)
router.register('goodimgs',GoodImgsViewSets)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 配置RestFul路由
    path('api/v1/',include(router.urls)),
    # API文档地址
    path('api/v1/docs',include_docs_urls(title='RestFulAPI',description='RestFulAPI v1')),
    # 在
    path('',include('rest_framework.urls')),

]
