from django.shortcuts import render


def users_home(request):
    return render(request, 'users/users_home.html', {'title': 'Users'})

def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})