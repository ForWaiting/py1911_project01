# Generated by Django 3.0.3 on 2020-02-25 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0002_auto_20200225_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ana',
            name='img',
            field=models.ImageField(upload_to='MyBlog/ana_img', verbose_name='微语配图'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='MyBlog/article_img', verbose_name='文章配图'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='img',
            field=models.ImageField(upload_to='MyBlog/comment_img', verbose_name='评论者头像'),
        ),
        migrations.AlterField(
            model_name='leavemes',
            name='img',
            field=models.ImageField(upload_to='MyBlog/lev_mes_img', verbose_name='留言配图'),
        ),
        migrations.AlterField(
            model_name='myskill',
            name='per_skill_img',
            field=models.ImageField(upload_to='MyBlog/per_skill_img', verbose_name='技能图谱'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='img',
            field=models.ImageField(upload_to='MyBlog/photo_img', verbose_name='相册'),
        ),
        migrations.AlterField(
            model_name='selfintroduction',
            name='img',
            field=models.ImageField(upload_to='MyBlog/personage_img', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='selfintroduction',
            name='wechat_img',
            field=models.ImageField(upload_to='MyBlog/wechat_img', verbose_name='微信二维码'),
        ),
        migrations.AlterField(
            model_name='viewpage',
            name='img',
            field=models.ImageField(upload_to='MyBlog/Imgview_page', verbose_name='页面视图'),
        ),
    ]