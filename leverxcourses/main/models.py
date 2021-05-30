from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class CourseGroup(models.Model):
    name = models.CharField('Name', max_length=20)
    image = models.ImageField('Image', max_length=20)


class Course(models.Model):
    name = models.CharField('Name', max_length=20)
    date = models.DateField('Date start')
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'


class Lecture(models.Model):
    theme = models.CharField('Theme', max_length=20)
    slides = models.FileField('Slides', upload_to=u'slides')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme

    def __unicode__(self):
        return u"file {0}".format(self.file.url)


class LectureTask(models.Model):
    name = models.CharField('Name', max_length=20)
    text = models.TextField('Text', max_length=250)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'


class TaskControl(models.Model):
    datetime = models.DateTimeField('DateTime', default=datetime.now())
    attachment = models.TextField('Homework')
    completed = models.BooleanField('Completed', default=False)
    checked = models.BooleanField('Checked', default=False)
    grade = models.SmallIntegerField('Grade', default=0)
    task = models.ForeignKey(LectureTask, on_delete=models.PROTECT)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return f'/'


class TaskComments(models.Model):
    comment = models.TextField('Comment', max_length=250)
    datetime = models.DateTimeField('DateTime', default=datetime.now())
    taskcontrol = models.ForeignKey(TaskControl, on_delete=models.PROTECT)

    def __str__(self):
        return self.datetime

    def get_absolute_url(self):
        return f'/'
