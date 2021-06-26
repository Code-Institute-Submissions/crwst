from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView, name='blogs'),
    path('blog/<int:_id>/', views.BlogDetailView, name='blog'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:_id>/', views.delete_blog, name='delete_blog'),
]
