from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView, name='blogs'),
    path('blog/<int:_id>', views.BlogDetailView, name='blog'),
    path('add/', views.add_blog, name='add_blog'),
]
