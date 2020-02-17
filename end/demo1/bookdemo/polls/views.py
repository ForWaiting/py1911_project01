from django.shortcuts import render,reverse,redirect
from .models import VoteInfo,VoteOption
# Create your views here.

def poll_index(request):

    polls = VoteInfo.objects.all()

    return render(request,'poll_index.html',{'polls':polls})

def poll_detail(request,voteid):
    vote_info = VoteInfo.objects.get(id=voteid)
    if request.method == "GET":
        return render(request,'poll_detail.html',{'vote_info':vote_info})
    elif request.method == "POST":
        vote_option = vote_info.voteoption_set.all()
        for voted in vote_option:
            if voted.content == request.POST.get("voted"):
                voted.vote_num += 1
                voted.save()
                break
        url = reverse("polls:poll_result",args=(voteid,))
        return redirect(to=url)

def poll_result(request,voteid):
    vote_info = VoteInfo.objects.get(id=voteid)
    return render(request,'poll_result.html',{'vote_info':vote_info})
    pass