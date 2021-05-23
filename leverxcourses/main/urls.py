from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('course', views.course, name='course'),
    path('lectures', views.lectures, name='lectures'),
    path('tasks', views.tasks, name='tasks')
]