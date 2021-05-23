from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home',
        'values': ['Vitali Kudzelka', '2','3']
    }
    return render(request, 'main/index.html',data)


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