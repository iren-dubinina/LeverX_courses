from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('lectures/', views.LectureList.as_view()),
    path('lectures/<int:pk>/', views.LectureDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('task_control/', views.TaskControlList.as_view()),
    path('task_control/<int:pk>/', views.TaskControlDetail.as_view()),
    path('task_comments/', views.TaskCommentsList.as_view()),
    path('task_comments/<int:pk>/', views.TaskCommentsDetail.as_view()),
    path('main', get_schema_view(
        title="Leverxcourses",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
