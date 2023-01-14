from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = loader.get_template('posts/index.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request))
    #Страница сообществ
def groups(request, slug):
    return HttpResponse('Страница сообществ')
    #Страница для постов
def group_list(request):
    return HttpResponse('Страница для постов')