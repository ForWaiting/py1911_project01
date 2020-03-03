from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品名')
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name='商品描述')
    #  在序列化关联模型一定要声明 relate_name

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类',related_name='goods')

    def __str__(self):
        return self.name

class GoodImg(models.Model):
    # 媒体资源
    img = models.ImageField(upload_to='goodimg',verbose_name='商品展示图')
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name='商品',related_name='imgs')

# 构建一个用户类
class User(AbstractUser):
    telephone = models.CharField(max_length=11,verbose_name='手机号')

# 商品订单
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    goods = models.ManyToManyField(Good,verbose_name='商品')
    pass