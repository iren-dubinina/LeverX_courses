from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Course, Lecture, Task
from .forms import CoursesForm, LectureForm, TaskForm
from django.views.generic import DetailView, UpdateView, ListView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'main/course_details.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'main/course_details.html'

    form_class = CourseDetailView


class CourseLecturesView(ListView):
    model = Lecture
    context_object_name = 'lectures'
    template_name = 'main/lectures.html'

    def get_context_data(self, **kwargs):
        context = super(CourseLecturesView, self).get_context_data(**kwargs)
        context['lectures'] = Lecture.objects.filter(course=self.kwargs.get('pk'))
        return context


class CourseTasksView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'main/tasks.html'

    def get_context_data(self, **kwargs):
        context = super(CourseTasksView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(course=self.kwargs.get('pk'))
        return context


def index(request):
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'courses': courses})


def course(request):
    data = {
        'title': 'Course'
    }
    return render(request, 'main/course.html', data)


def lectures(request):
    lectures = Lecture.objects.all()
    print('lectures', lectures)
    return render(request, 'main/lectures.html', {'lectures': lectures})


def lecture_details(request):
    lectures = Lecture.objects.all()
    print('lectures', lectures)
    return render(request, 'main/lecture_details.html', {'lectures': lectures})


def tasks(request):
    data = {
        'title': 'Tasks'
    }
    return render(request, 'main/tasks.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = CoursesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


def create_lecture(request):
    error = ''
    if request.method == 'POST':
        print(request.FILES)
        form = LectureForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = LectureForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_lecture.html', data)


def create_task(request):
    error = ''
    if request.method == 'POST':
        print(request.FILES)
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = TaskForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', data)
