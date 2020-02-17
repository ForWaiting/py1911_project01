from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from .models import VoteInfo, VoteOption
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.
# View类为所有的视图响应基类


# 基于视图函数FBV实现主页
def poll_index(request):
    polls = VoteInfo.objects.all()
    return render(request, 'poll_index.html', {'polls': polls})


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
        return render(request, 'poll_detail.html', {'vote_info': vote_info})
    elif request.method == "POST":
        vote_option = vote_info.voteoption_set.all()
        for voted in vote_option:
            if voted.content == request.POST.get("voted"):
                voted.vote_num += 1
                voted.save()
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
