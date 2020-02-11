from django.db import models


# Create your models here.
# 有了模型类之后模型类如何与数据库交互
# 1.注册模型 在setting.py 中的INSTALLED_APPS 添加应用名 booktest
# 2.生成迁移文件 用于与数据库交互 python manage.py makemigrations 会在对应应用下方生成迁移文件 不需要关注
# 3.执行迁移 会在对应的数据库生成对应的表 python manage.py migrate
# 模型类更改之后需要再次生成迁移文件执行迁移
class Book(models.Model):
    """
    book继承了Model类 应为Model 类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")
    price = models.FloatField(default=0)
    pass

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    Hero 继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="male")
    content = models.CharField(max_length=100)
    # book是一对多中的外键 on_delete代表删除主表数据时如何做，models.CASCADE 代表级联效应  删除主键连同外键一起删除
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    pass

    def __str__(self):
        return self.name


# django orm 关联查询
# 多方Hero  一方Book
# 1.多找一， 多方对象，关系字段       exp：h1.book
# 2. 一找多，  一方对象，小写多方类名_set.all()   exp : b1.hero_set.all()
