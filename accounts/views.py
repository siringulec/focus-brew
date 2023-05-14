from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from accounts.forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
