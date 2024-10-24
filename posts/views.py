from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.db.models import Q
from posts.forms import PostForm2, SearchForm

def answer_view(request):
    return HttpResponse("<h1>My answer:</h1>")
# Create your views here.
def second_view(request):
    return render(request, 'base.html')

@login_required(login_url='/login/')
def list_view(request):
    limit = 3
    if request.method == "GET":
        search = request.GET.get('search', None)
        tag = request.GET.get('tag', None)
        ordering = request.GET.get('ordering', None)
        posts = Post.objects.all()
        page = int(request.GET.get('page', 1))

        if search:
            posts = posts.filter (Q(title__icontains=search) | Q(content__icontains=search))
        if tag:
            posts = posts.filter(tags__id__in=tag)
        if ordering:
            posts = posts.order_by(ordering)
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

            start = (page - 1) * limit
            end = page * limit
            posts = posts[start:end]
        form = SearchForm()
        context = {'posts': posts, 'form': form, 'max_pages': range(1, max_pages + 1)}
        return render(request, 'posts/list.html', context=context)

@login_required(login_url='/login/')
def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', {'form': form})
        form.save()
        return HttpResponse(f'Created post')
