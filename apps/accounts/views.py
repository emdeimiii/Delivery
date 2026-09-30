from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .form import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('catalogs:dish_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})