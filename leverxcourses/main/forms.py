from django.contrib.auth.models import User

from .models import Course, Lecture, LectureTask, CourseGroup, TaskControl, TaskComments
from django.forms import ModelForm, TextInput, DateInput, FileInput, Select, Textarea, CheckboxSelectMultiple, \
    SelectMultiple, ImageField, FileField, NullBooleanSelect


class CoursesForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'date', 'group']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сourse name'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start date'
            }),
            "group": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Group name'
            }),
        }


class CourseGroup(ModelForm):
    img = ImageField()

    class Meta:
        model = CourseGroup
        fields = ['name', 'img']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сourse name'
            })
        }


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'slides', 'course']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lecture name'
            }),
            "slides": FileInput(attrs={
                'type': 'file'
            }),
            "course": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Course'
            })
        }


class TaskForm(ModelForm):
    class Meta:
        model = LectureTask
        fields = ['name', 'text', 'lecture']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task name'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "lecture": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Course'
            })
        }


class AddUserForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'users', 'date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task name'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start date'
            }),
            "users": SelectMultiple()
        }


class TaskControlForm(ModelForm):
    class Meta:
        model = TaskControl
        fields = ['datetime', 'attachment', 'completed', 'task']

        widgets = {
            "task": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Completed'
            }),
            "datetime": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'DateTime'
            }),
            "attachment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Reference"
            }),
            "completed": NullBooleanSelect(attrs={
                'class': 'form-control',
                'placeholder': 'Completed'
            })
        }


class TaskCommentsForm(ModelForm):
    class Meta:
        model = TaskComments
        fields = ['datetime', 'comment', 'taskcontrol']

        widgets = {
            "datetime": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'DateTime'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reference'
            }),
            "taskcontrol": Select(attrs={
                'class': 'form-control',
            }),
        }
