from django.urls import path
from . import views
app_name ='posts'

urlpatterns = [
    #Главная страница
    path('', views.index),
    #Страница сообществ
    path('group_list/<slug:slug>/',views.group_list),
    #Страница для постов
    path('group_list/<any_dlug>/',views.group_list)
]
