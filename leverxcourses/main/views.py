from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'courses' : courses})


def course(request):
    data = {
        'title': 'Course'
    }

    return render(request, 'main/course.html', data)


def lectures(request):
    data = {
        'title': 'Lectures'
    }

    return render(request, 'main/lectures.html', data)


def tasks(request):
    data = {
        'title': 'Tasks'
    }

    return render(request, 'main/tasks.html', data)

def create(request):
    return render(request, 'main/create.html')
