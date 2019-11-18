from django.shortcuts import render  # render позволяет выводить прописанный в отдельном файле код html


# from django.http import HttpResponse
# HttpResponse позволяет выводить html-код, встроенный конкретно в этот питон-файла (сойдет, если html-кода немного)

def base(request):
    return render(request, 'start_page/home.html')
