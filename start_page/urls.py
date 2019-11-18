from django.urls import path
from . import views

urlpatterns = [  # Ссылка второго уровня для страницы start_page
    path('', views.base, name='start_page-base'),  # Если за .../start_page/ больше ничего не написано
]
