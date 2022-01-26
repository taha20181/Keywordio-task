from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view, name='student_view'),
    
    path('lms/', views.index, name='index'),
    
    path('add_book/', views.add_book, name='add_book'),
    path('show_books/', views.show_books, name='show_books'),
    path('update_book/<str:pk>/', views.update_book, name='update_book'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
]