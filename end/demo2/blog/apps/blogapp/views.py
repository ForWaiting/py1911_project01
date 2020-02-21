from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Page,Paginator
# Create your views here.

def index(request):
    ads = Ads.objects.all()
    typepage = request.GET.get('type')
    year = None
    month = None
    if typepage == 'date':
        year = request.GET.get('year')
        month = request.GET.get('month')
        articles = Article.objects.filter(create_time__year = year,create_time__month=month).order_by('-create_time')
    else:
        articles = Article.objects.all()
    paginator = Paginator(articles,2)
    num = request.GET.get('pagenum',1)
    page = paginator.get_page(num)
    # locals可以返回作用域局部变量
    return render(request,'index.html',{'ads':ads,'page':page,'type':typepage,'year':year,'month':month})


def detail(request,articleid):

    return render(request,'single.html')


def contact(request):

    return render(request,'contact.html')

def favicon(request):
    return redirect(to='/static/favicon.ico')