from django.contrib.auth.models import User

from .models import Course, Lecture, Task
from django.forms import ModelForm, TextInput, DateInput, FileInput, Select, Textarea, CheckboxSelectMultiple


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
            "group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Group name'
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
        model = Task
        fields = ['name', 'text', 'course']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task name'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "course": Select(attrs={
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
            "users": CheckboxSelectMultiple()
        }
