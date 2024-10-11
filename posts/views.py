from django.shortcuts import render
from django.http import HttpResponse
from posts.models import post

def answer_view(request):
    return HttpResponse("<h1>My answer:</h1>")
# Create your views here.
def second_view(request):
    return render(request, 'base.html')

def list_view(request):
    posts = post.objects.all
    return render(request, 'list.html', {'posts': posts})

def detail_view(request, post_id):
    posts_2 = post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'posts_2': posts_2})
