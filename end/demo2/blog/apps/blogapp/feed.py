# -*- encoding: utf-8 -*-
"""
@File    : feed.py
@Time    : 2020/2/21 15:38
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
# 使用Django框架集成的Rss
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Article

class ArticleFeed(Feed):
    title = 'WEB全栈开发技术'
    description = '定期发布一些web全栈开发技术'
    link = '/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        # return '/detail/'+item.id +'/'
        url = reverse('blogapp:detail',args=(item.id,))
        return url