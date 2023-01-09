from django.shortcuts import render
from django.http import HttpResponse

#С помощью функции render() подключаем
# шаблон к соответствующей view-функции.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

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