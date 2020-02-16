from django.contrib import admin
# 定义后端显示界面
from django.contrib.admin import ModelAdmin

# Register your models here.
# django 自带的后台管理操作需要在此实现

# 注册自己需要管理的模型 Book Hero

from .models import Book, Hero, User


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender')


class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 2


class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台界面
    """
    list_display = ('title', 'price', 'pub_date')
    # 每页显示1个
    list_per_page = 5
    # 定义搜索字段
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(User)
