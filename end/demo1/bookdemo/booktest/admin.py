from django.contrib import admin

# Register your models here.
# django 自带的后台管理操作需要在此实现

# 注册自己需要管理的模型 Book Hero

from .models import Book,Hero
admin.site.register(Book)
admin.site.register(Hero)

