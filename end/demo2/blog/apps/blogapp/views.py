from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from .models import *
from django.core.paginator import Page,Paginator
from blogapp.forms import CommentForm
# Create your views here.

def index(request):
    ads = Ads.objects.all()
    typepage = request.GET.get('type')
    year = None
    month = None
    category_id = None
    if typepage == 'date':
        year = request.GET.get('year')
        month = request.GET.get('month')
        articles = Article.objects.filter(create_time__year = year,create_time__month=month).order_by('-create_time')
    elif typepage == 'category':
        category_id = request.GET.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('分类不和法')
    elif typepage == 'tag':
        tag_id = request.GET.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('标签不合法')
    else:
        articles = Article.objects.all()
    paginator = Paginator(articles,2)
    num = request.GET.get('pagenum',1)
    page = paginator.get_page(num)
    # locals可以返回作用域局部变量
    return render(request,'index.html',locals())
    # return render(request,'index.html',{'ads':ads,'page':page,'type':typepage,'year':year,'month':month})


def detail(request,articleid):
    if request.method == 'GET':
        try:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            return render(request,'single.html',locals())
        except Exception as e:
            print(e)
            return HttpResponse('文章不合法')
    elif request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse('blogapp:detail',args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = '输入信息有错误'
            return render(request,'single.html')


def contact(request):

    return render(request,'contact.html')

def favicon(request):
    return redirect(to='/static/favicon.ico')