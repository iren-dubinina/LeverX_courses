from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField('Name', max_length=20)
    date = models.DateField('Date start')
    group = models.CharField('Group', max_length=1)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'


class Lecture(models.Model):
    name = models.CharField('Name', max_length=20)
    slides = models.FileField('Slides')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'


class Task(models.Model):
    name = models.CharField('Name', max_length=20)
    text = models.TextField('Text', max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'


class LectureTask(models.Model):
    name = models.CharField('Name', max_length=20)
    text = models.TextField('Text', max_length=250)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'
