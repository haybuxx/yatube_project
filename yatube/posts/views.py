from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Ты <i>не можешь</i> получить'
                        ' правильные <b>ответы</b>,<br> '
                        'если у тебя нет правильных '
                        '<s>вопросов</s> запросов.'
    )


def group_posts(request):
    return HttpResponse('Посты')


def posts_detail(request, slug):
    return HttpResponse('Здесь будут отображаться посты')