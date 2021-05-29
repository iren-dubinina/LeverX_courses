from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Course, Lecture, LectureTask, TaskControl
from .forms import CoursesForm, LectureForm, TaskForm, AddUserForm, CourseGroup, TaskControlForm
from django.views.generic import DetailView, UpdateView, ListView, DeleteView

User = get_user_model()


# content_type = ContentType.objects.get(app_label='main', model='Course')
# permission = Permission.objects.create(codename='can_add',
#                                        name='Can Publish Posts',
#                                        content_type=content_type)
# group = Group.objects.get(name='lecturer')
# group.permissions.add(permission)

# pers = Permission.objects.filter(codename__contains='user')
# group = Group.objects.get(name='lecturer')
# group.permissions.add(per)

# per = Permission.objects.filter(codename__contains='course')
# group = Group.objects.get(name='lecturer')
# group.permissions.add(per)

# pers = Permission.objects.filter(codename__contains='lecture')
# group = Group.objects.get(name='lecturer')
# for per in pers:
#     group.permissions.add(per)

# pers = Permission.objects.filter(codename__contains='task')
# group = Group.objects.get(name='lecturer')
# for per in pers:
#     group.permissions.add(per)


# TODO move groups permissions to another file
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
    success_url = '/'
    template_name = 'main/delete_course.html'


class TaskcontrolDeleteView(DeleteView):
    model = Course
    success_url = '/'
    template_name = 'main/delete_course.html'


class TaskcontrolUpdateView(UpdateView):
    model = TaskControl
    template_name = 'main/create_lecture.html'
    form_class = TaskControlForm


class LectureUpdateView(UpdateView):
    model = Lecture
    template_name = 'main/create_lecture.html'
    form_class = LectureForm


class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = '/'
    template_name = 'main/delete_lecture.html'


class LectureTaskUpdateView(UpdateView):
    model = LectureTask
    template_name = 'main/create_task.html'
    form_class = TaskForm


class LectureTaskDeleteView(DeleteView):
    model = LectureTask
    success_url = '/'
    template_name = 'main/delete_task.html'


class CourseLecturesView(ListView):
    model = Lecture
    template_name = 'main/lectures.html'  # обработчик
    context_object_name = 'lecture'  # ключ объекта, кот. передается в шаблон

    def get_context_data(self, **kwargs):
        context = super(CourseLecturesView, self).get_context_data(**kwargs)
        context['lectures'] = Lecture.objects.filter(course=self.kwargs.get('pk'))
        context['course_id'] = self.kwargs.get('pk')
        return context


class CourseTasksView(ListView):
    model = LectureTask
    template_name = 'main/tasks.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(CourseTasksView, self).get_context_data(**kwargs)
        context['tasks'] = LectureTask.objects.filter(lecture=self.kwargs.get('pk'))
        context['lecture'] = self.kwargs.get('pk')
        return context


class LectureTasksControlView(ListView):
    model = TaskControl
    template_name = 'main/taskcontrol.html'
    context_object_name = 'taskcontrol'

    def get_context_data(self, **kwargs):
        context = super(LectureTasksControlView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        context['taskscontrols'] = TaskControl.objects.filter(task=self.kwargs.get('pk')).filter(users__id=user_id)
        context['task_id'] = self.kwargs.get('pk')
        # context['users'] = self.kwargs.get('pk')
        return context


def getCourseById(pk):
    course = Course.objects.filter(id=pk).values()[0]
    print(course)
    return course


def getUsersByCourse(pk):
    users = User.objects.filter(course__id=pk)
    print(users)
    return users


@login_required(login_url='/users/login')
def course_users(request, pk):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            course = Course.objects.get(id=pk)
            for user in form.cleaned_data['users']:
                course.users.add(user)
            return redirect('course_users', pk)
    form = AddUserForm(initial=getCourseById(pk))
    course = getCourseById(pk)
    users = getUsersByCourse(pk)
    return render(request, 'main/course_users.html', {'form': form, 'course': course, 'users': users})


@login_required(login_url='/users/login')
def index(request):
    courses = []
    courses = Course.objects.filter(users__id=request.user.id)
    return render(request, 'main/index.html', {'courses': courses})


@login_required(login_url='/users/login')
def course(request):
    data = {
        'title': 'Course'
    }
    return render(request, 'main/course.html', data)


@login_required(login_url='/users/login')
def LectureTasks(request):
    data = {
        'title': 'Tasks'
    }
    return render(request, 'main/tasks.html', data)


@login_required(login_url='/users/login')
@permission_required('main.add_course')
def create(request):
    error = ''
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.users.add(request.user)
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = CoursesForm(initial={'users': User.objects.filter(id=request.user.id)})
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


@login_required(login_url='/users/login')
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


@login_required(login_url='/users/login')
def create_task(request, pk):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks', pk)
        else:
            error = 'Form is not valid'

    form = TaskForm(initial={'lecture': Lecture.objects.get(id=pk)})
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', data)


@login_required(login_url='/users/login')
def add_group(request):
    error = ''
    if request.method == 'POST':
        form = CourseGroup(request.POST, request.FILES)
        print(request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = CourseGroup()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_group.html', data)


def add_taskcontrol(request, pk):
    error = ''
    if request.method == 'POST':
        form = TaskControlForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            taskcontrol = form.save()
            taskcontrol.users.add(request.user)
            return redirect('taskcontrol', pk)
        else:
            error = 'Form is not valid'

    form = TaskControlForm(initial={'task': LectureTask.objects.get(id=pk)})
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_taskcontrol.html', data)
