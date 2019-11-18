"""Main_Directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_accounts import views as user_account_views
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  # Ссылки первого уровня
    path('admin/', admin.site.urls),  # Панель админа
    path('start_page/', include('start_page.urls')),  # Стартовая страница
    path('quest_list/', include('quest_list.urls')),  # Домашняя (главная) страница
    path('', include('quest_list.urls')),  # Та же самая домашняя (главная) страница в случае отсутствия ссылки 1 уровня
    path('auth/', authViews.LoginView.as_view(template_name='user_accounts/auth.html'), name='auth'),  # Страница входа
    path('exit/', authViews.LogoutView.as_view(template_name='user_accounts/exit.html'), name='exit'),  # Страница выхода
    path('reg/', user_account_views.register, name='reg'),  # Страница регистрации
    path('profile/', user_account_views.profile, name='profile'),  # Страница профиля
]

if settings.DEBUG:  # Статические файлы подключаются только в режиме отладки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
