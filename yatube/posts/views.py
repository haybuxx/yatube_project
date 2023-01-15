from django.shortcuts import render, get_object_or_404
from .models import Post, Group

#Кол-во отображаемых постов
POST_VIEW_COUNT = 10

def index(request):
    posts = Post.objects.all()[:POST_VIEW_COUNT]
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.group.all()[:POST_VIEW_COUNT]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)