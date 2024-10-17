from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm, PostForm2

def answer_view(request):
    return HttpResponse("<h1>My answer:</h1>")
# Create your views here.
def second_view(request):
    return render(request, 'base.html')

def list_view(request):
    posts = Post.objects.all
    return render(request, 'list.html', {'posts': posts})

def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post_create.html', {'form': form})
        form.save()
        return HttpResponse(f'Created post')
