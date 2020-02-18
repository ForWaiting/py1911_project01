from django.contrib.auth import authenticate,login as lin,logout as lot
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from .models import VoteInfo, VoteOption, User
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.
# View类为所有的视图响应基类


# 基于视图函数FBV实现主页
def poll_index(request):
    polls = VoteInfo.objects.all()
    items = None
    return render(request, 'poll_index.html', {'polls': polls,'name':'<h2>二级标题hzf<h2>','items':items})


# 基于CBV形式实现主页
class PollIndexView(ListView):
    # 第一种方法继承    ListView
    # template_name 指名使用的模板
    template_name = "poll_index.html"
    # queryset 指明返回的结果列表
    queryset = VoteInfo.objects.all()
    # context_object_name 指明返回的字典参数的键
    context_object_name = "polls"

    # 第二种方法继承    TemplateView
    # template_name = "poll_index.html"
    # 重写父类函数
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return {'polls':VoteInfo.objects.all()}


def poll_detail(request, voteid):
    vote_info = VoteInfo.objects.get(id=voteid)
    if request.method == "GET":
        if request.user and request.user.username != "":
            if vote_info in request.user.voteinfo.all():
                url = reverse('polls:poll_result',args=(voteid))
                return redirect(to=url)
            else:
                return render(request, 'poll_detail.html', {'vote_info': vote_info})
        else:
            url = reverse('polls:login')+"?next=/polls/polldetail/"+voteid
            return redirect(to=url)
    elif request.method == "POST":
        vote_option = vote_info.voteoption_set.all()
        for voted in vote_option:
            if voted.content == request.POST.get("voted"):
                voted.vote_num += 1
                voted.save()
                request.user.voteinfo.add(VoteInfo.objects.get(id=voteid))
                break
        url = reverse("polls:poll_result", args=(voteid,))
        return redirect(to=url)

# 基于CBV形式实现详情页
class PollDetailView(View):
    def get(self, request, voteid):
        vote_info = VoteInfo.objects.get(id=voteid)
        return render(request, 'poll_detail.html', {'vote_info': vote_info})

    def post(self, request, voteid):
        vote_info = VoteInfo.objects.get(id=voteid)
        vote_option = vote_info.voteoption_set.all()
        for voted in vote_option:
            if voted.content == request.POST.get("voted"):
                voted.vote_num += 1
                voted.save()
                break
        url = reverse("polls:poll_result", args=(voteid,))
        return redirect(to=url)


def poll_result(request, voteid):
    vote_info = VoteInfo.objects.get(id=voteid)
    return render(request, 'poll_result.html', {'vote_info': vote_info})
    pass

# 基于CBV形式实现结果页
class PollResultView(View):
    def get(self, request, voteid):
        vote_info = VoteInfo.objects.get(id=voteid)
        return render(request, 'poll_result.html', {'vote_info': vote_info})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            lin(request,user)
            next = request.GET.get('next')
            if next:
                url = next
            else:
                url = reverse('polls:poll_index')
            return redirect(to=url)
        else:
            url = reverse('polls:login')
            return redirect(to=url)
def regist(request):
    if request.method == 'GET':
        return render(request,'regist.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(User.objects.filter(username=username))> 0:
            return HttpResponse('用户名已经存在')
        else:
            if password != password2:
                return HttpResponse('两次密码不一致')
            else:
                User.objects.create_user(username=username,password=password)
                url = reverse('polls:login')
                return redirect(to=url)
def logout(request):
    lot(request)
    url = reverse('polls:poll_index')
    return redirect(to=url)