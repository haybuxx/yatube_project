# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    #Главная страница
    path('', views.index),
    # Для страницы, на которой будут посты, отфильтрованные по группам
    path('posts/', views.group_posts),
    # Полученные данные запишем в переменную
    path(
        'group/<slug:slug>/',
        views.posts_detail
    ),
]