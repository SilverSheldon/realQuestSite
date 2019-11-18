from django.shortcuts import render  # render позволяет выводить прописанный в отдельном файле код html
from .models import QuestList


# from django.http import HttpResponse
# HttpResponse позволяет выводить html-код, встроенный конкретно в этот питон-файла (сойдет, если html-кода немного)

def base(request):
    data = {
        'quest': QuestList.objects.all(),
        'title': 'Главная страница',
    }
    return render(request, 'quest_list/quest_list.html', data)
