from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Course, Lecture, Task
from .forms import CoursesForm, LectureForm, TaskForm
from django.views.generic import DetailView, UpdateView, ListView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'main/course_details.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'main/create.html'
    form_class = CoursesForm


class CourseDeleteView(DeleteView):
    model = Course
    success_url = 'main/index.html'
    template_name = 'main/delete_course.html'


class LectureUpdateView(UpdateView):
    model = Lecture
    template_name = 'main/create_lecture.html'
    form_class = LectureForm


class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = 'main/index.html'
    template_name = 'main/delete_lecture.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create_task.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = 'main/index.html'
    template_name = 'main/delete_task.html'


class CourseLecturesView(ListView):
    model = Lecture
    template_name = 'main/lectures.html'  # обработчик
    context_object_name = 'lecture'  # ключ объекта, кот. передается в шаблон

    def get_context_data(self, **kwargs):
        context = super(CourseLecturesView, self).get_context_data(**kwargs)
        context['lectures'] = Lecture.objects.filter(course=self.kwargs.get('pk'))
        return context


class CourseTasksView(ListView):
    model = Task
    template_name = 'main/tasks.html'  # обработчик
    context_object_name = 'task'  # ключ для передачи в шаблон

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
