from django.shortcuts import render, redirect
from .forms import RegistrationForm


def users_home(request):
    return render(request, 'users/users_home.html', {'title': 'Users'})


def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})


def registration(request):
    error = ''
    if request.method == 'POST':
        print(request.FILES)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = RegistrationForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'users/users_home.html', {})
