from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Book,Hero
def index(response):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    # template = loader.get_template('index.html')
    # 2.渲染模板数据
    books = Book.objects.all()
    # context = {'books':books}
    # result = template.render(context)
    # 3.将渲染的结果 HttpResponse返回
    # return HttpResponse(result)

    # 3步合成一部
    return render(response,'index.html',{'books':books})
def detail(response,bookid):
    # return HttpResponse("这里是详情页"+ bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id = bookid)
    # context = {'book':book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(response,'detail.html',{'book':book})
def about(response):
    return HttpResponse("这里是关于")