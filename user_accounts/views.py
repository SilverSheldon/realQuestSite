from django.shortcuts import render, redirect
from .forms import UserAccReg
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserAccReg(request.POST)
        if form.is_valid():  # Проверка, заполнена ли форма, чтоб в дальнейшем переадресовать или вывести "зареган"
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Добро пожаловать, игрок {username}!')
            return redirect('auth')  # Переадресация на главную
    else:
        form = UserAccReg()
    return render(request, 'user_accounts/registration.html', {'form': form, 'title': 'Регистрация'})


@login_required
def profile(request):
    return render(request, 'user_accounts/profile.html')
