from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import SignUpForm


def users_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            groups = form.cleaned_data.get('groups')
            print(groups)
            for group in groups:
                my_group = Group.objects.get(name=group)
                my_group.user_set.add(user)
            login(request, user)
            return redirect('swagger-ui')
    else:
        form = SignUpForm()
    return render(request, 'users/registration.html', {'title': 'Users', 'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('swagger-ui')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'title': 'Login', 'form': form})
