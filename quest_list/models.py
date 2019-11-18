from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''Подключение базы данных (таблицы), связанной с конкретным приложением осуществляется в директории оного,
в файле models.py. Прописывается класс с названием таблицы, где его поля (переменные) являются колонками таблицы.'''


class QuestList(models.Model):
    QUEST_TYPE_CHOICES = (
        ("ONCE", 'Разовый'),
        ("REGULAR", 'Регулярный'),
        ("DAILY", 'Ежедневный'),
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    quest_name = models.TextField(max_length=50)
    quest_type = models.TextField(choices=QUEST_TYPE_CHOICES)  # Надо, чтоб поле deadline работало соответственно
    tags = models.CharField(max_length=50, blank=True)
    quest_description = models.TextField()
    reward = models.TextField(max_length=50, blank=True)
    XP_reward = models.IntegerField()
    XP_penalty = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.quest_name

'''После создания таблицы, в командном окне прописать python manage.py makemigrations, после чего в папке migrations
создается файл (в данном случае 0001). 
Проверить SQL-код таблицы можно командой python manage.py sqlmigrate home_page 0001
После этого использовать команду python manage.py migrate
Чтобы таблица отображалась в админке сайта, надо в этой же директории приложения открыть файл admin.py
и импортировать из этой же директории данного приложения название таблицы (класса)'''
