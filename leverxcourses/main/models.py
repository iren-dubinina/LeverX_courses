from django.db import models


class Course(models.Model):
    name = models.CharField('Name', max_length=20)
    date = models.DateField('Date start')
    group = models.CharField('Group', max_length=1)

    def __str__(self):
        return self.name