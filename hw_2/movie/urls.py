from django.urls import path
from . import views
from .views import get_movies

urlpatterns = [
    path('', views.get_movies, name='get_movies'),
    path('<int:id>/', views.get_movie_by_id, name='movie-detail'),
]