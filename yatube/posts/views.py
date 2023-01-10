from django.shortcuts import render
from django.http import HttpResponse

#С помощью функции render() подключаем
# шаблон к соответствующей view-функции.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request):
    return HttpResponse('Посты')


def posts_detail(request, slug):
    return HttpResponse('Здесь будут отображаться посты')

# Create your views here.
#def index(request_2):
#    return HttpResponse('Ты <i>не можешь</i> получить'
#                        ' правильные <b>ответы</b>,<br> '
#                        'если у тебя нет правильных '
#                        '<s>вопросов</s> запросов.'
#    )

#def index(request_3):
#    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
#    template = 'posts/index.html'
#    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
#    title = 'Это главная страница проекта Yatube'
#    # Словарь с данными принято называть context
#    context = {
#        # В словарь можно передать переменную
#        'title': title,
#        # А можно сразу записать значение в словарь. Но обычно так не делают
#        'text': 'Главная страница',
#    }
#    # Третьим параметром передаём словарь context
#    return render(request_3, template, context)

#def group_posts(request_3):
#    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
#    template = 'posts/index.html'
#    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
#    title = 'десь будет информация о группах проекта Yatube'
#    # Словарь с данными принято называть context
#    context = {
#        # В словарь можно передать переменную
#        'title': title,
#        # А можно сразу записать значение в словарь. Но обычно так не делают
#        'text': 'Главная страница',
#    }
#    # Третьим параметром передаём словарь context
#    return render(request_3, template, context)

