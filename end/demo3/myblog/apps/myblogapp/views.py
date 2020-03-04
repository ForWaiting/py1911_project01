from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# 导入django自带的分页模块
from django.core.paginator import Page,Paginator

# Create your views here.

# 首页
def index(request):
    type = request.GET.get('type')
    user = SelfIntroduction.objects.all()[0]
    # 创建一个分页器
    if type == 'category':
        category_id = request.GET.get('category_id')
        try:
            category = Category.objects.get(id = category_id)
            article = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('分类错误')
    else:
        article = Article.objects.all().order_by('-create_time')
    paginator = Paginator(article, 2)
    num = request.GET.get('pagenum', 1)
    page = paginator.get_page(num)
    return render(request,'index.html',locals())

# 详情
def details(request,articleid):
    article = Article.objects.get(id=articleid)
    return render(request,'details.html',locals())

# 微语
def whisper(request):
    return render(request,'whisper.html')
    pass

# 留言
def leacots(request):
    return render(request,'leacots.html')

    pass

# 相册
def album(request):
    return render(request,'album.html')

    pass

#关于
def about(request):
    return render(request,'about.html')

    pass

def favicon(request):
    return redirect(to='/static/favicon.ico')