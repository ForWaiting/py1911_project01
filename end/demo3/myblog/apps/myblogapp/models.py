from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

# 博客主视图
class ViewPage(models.Model):
    img = models.ImageField(upload_to='MyBlog/Imgview_page', verbose_name='页面视图')
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name='视图描述')

    def __str__(self):
        return self.desc



# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    img = models.ImageField(upload_to='MyBlog/article_img', verbose_name='文章配图')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    page_view = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # body = models.TextField(verbose_name='正文')
    body = UEditorField(imagePath='imgs/',width='100%')
    def __str__(self):
        return self.title


# 文章评论
class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='评论者')
    img = models.ImageField(upload_to='MyBlog/comment_img', verbose_name='评论者头像')
    body = models.CharField(max_length=500, verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章评论')
    ana = models.ForeignKey('Ana', on_delete=models.CASCADE, verbose_name='微语评论')
    leavemes = models.ForeignKey('LeaveMes', on_delete=models.CASCADE, verbose_name='留言')

    def __str__(self):
        return self.name


# 微语
class Ana(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    img = models.ImageField(upload_to='MyBlog/ana_img', verbose_name='微语配图')
    like_num = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    comment_num = models.PositiveIntegerField(default=0, verbose_name='评论数')
    # body = models.CharField(max_length=500, verbose_name='微语正文')
    body = UEditorField(imagePath='imgs/',width='100%')

class LeaveMes(models.Model):
    img = models.ImageField(upload_to='MyBlog/lev_mes_img', verbose_name='留言配图')

# 相册
class PhotoAlbum(models.Model):
    img = models.ImageField(upload_to='MyBlog/photo_img', verbose_name='相册')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_site = models.CharField(max_length=15, verbose_name='创建地点')
    desc = models.CharField(max_length=50, verbose_name='描述')

    def __str__(self):
        return self.desc

# 个人介绍
class SelfIntroduction(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.PositiveIntegerField(default=18, verbose_name='年龄')
    profession = models.CharField(max_length=30, verbose_name='职业')
    hobby = models.CharField(max_length=100, verbose_name='爱好')
    img = models.ImageField(upload_to='MyBlog/personage_img', verbose_name='头像')
    wechat_num = models.CharField(max_length=20, default='hzf19960922', verbose_name='微信')
    wechat_img = models.ImageField(upload_to='MyBlog/wechat_img', verbose_name='微信二维码')
    qq_num = models.CharField(max_length=20, default='1677508764', verbose_name='QQ')
    phone = models.CharField(max_length=20, default='18337391053', verbose_name='电话')
    email = models.EmailField(default='huangzhenfang2017@163.com', verbose_name='个人邮箱')

    def __str__(self):
        return self.name

class MySkill(models.Model):
    name = models.CharField(max_length=20,verbose_name='技能名称')
    per_skill_img = models.ImageField(upload_to='MyBlog/per_skill_img', verbose_name='技能图谱')
    per_skillful = models.FloatField(default=0.8, verbose_name='技能熟练')
    selfIntroduction = models.ForeignKey(SelfIntroduction,on_delete=models.CASCADE,verbose_name='个人技能')

    def __str__(self):
        return self.name

