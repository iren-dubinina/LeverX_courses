from django.contrib.auth.models import User

from .models import Course, Lecture, LectureTask, CourseGroup, TaskControl
from django.forms import ModelForm, TextInput, DateInput, FileInput, Select, Textarea, CheckboxSelectMultiple, \
    SelectMultiple, ImageField, FileField, NullBooleanSelect


class CoursesForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сourse name'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start date'
            }),
        }


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ['theme', 'slides', 'course']

        widgets = {
            "theme": TextInput(attrs={
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
            }),
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
            }),
            "task": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Completed'
            })
        }
