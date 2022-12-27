from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Посты')


def posts_detail(request, slug):
    return HttpResponse('Здесь будут отображаться посты')