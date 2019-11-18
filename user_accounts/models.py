from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='profile_default.jpg', upload_to='user_image')  # Не выводится дефолтное изображение

    def __str__(self): """Метод определяет как в админке будут отображаться объекты бд"""
        return f'{self.user.username}'
