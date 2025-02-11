from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_threads, name='home'),
    path('threads/', views.thread_list, name='thread_list'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:id>/edit/', views.edit_thread, name='edit_thread'),
    path('threads/<int:id>/delete/', views.delete_thread, name='delete_thread'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
]