from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('admin/login/', views.login_view, name='login_view'),
    path('admin/register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout")
]