from django.urls import path
from . import views

urlpatterns = [  # Ссылка второго уровня для страницы quest_list
    path('', views.base, name='quest_list-base'),  # Если за .../quest_list/ больше ничего не написано
]