from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

app_name = 'authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/sign-up/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
