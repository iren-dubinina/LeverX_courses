from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('course', views.course, name='course'),
    url(r'^lecture/(?P<pk>\d+)/$', views.CourseLecturesView.as_view(), name='lectures'),
    url(r'^task/(?P<pk>\d+)/$', views.CourseTasksView.as_view(), name='tasks'),
    # path('tasks', views.tasks, name='tasks'),
    path('create', views.create, name='create'),
    path('create_lecture', views.create_lecture, name='create_lecture'),
    path('create_task', views.create_task, name='create_task'),
    path('<int:pk>', views.CourseDetailView.as_view(), name='course_details'),
    path('<int:pk>/update', views.CourseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CourseDeleteView.as_view(), name='delete'),
    path('<int:pk>/update_lecture', views.LectureUpdateView.as_view(), name='update_lecture'),
    path('<int:pk>/delete_lecture', views.LectureDeleteView.as_view(), name='delete_lecture'),
    path('<int:pk>/update_task', views.TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete_task', views.TaskDeleteView.as_view(), name='delete_task'),
    path('<int:pk>/course_users', views.course_users, name='course_users')
]
