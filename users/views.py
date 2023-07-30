from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан пользователь с именем {username}')
            return redirect('market-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_upd_form = UserUpdateForm(request.POST, instance = request.user)
        if user_upd_form.is_valid():
            user_upd_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        user_upd_from = UserUpdateForm(instance = request.user)

        context = {
            'u_form': user_upd_from
        }
    return render(request, 'users/profile.html', context)