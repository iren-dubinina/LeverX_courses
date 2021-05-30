from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.users_signup, name='users_home'),
    path('login', views.sign_in, name='login'),
    path('logout', views.logout_user, name='logout')
]