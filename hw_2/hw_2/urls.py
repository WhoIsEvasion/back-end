"""
URL configuration for hw_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from movie.views import get_movies, get_movie_by_id
from blog.views import get_articles, get_article_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', get_movies, name='get_movies'),
    path('movies/<int:id>/', get_movie_by_id, name='get_movie_by_id'),
    path('articles/', get_articles, name='get_articles'),
    path('articles/<int:id>/', get_article_by_id, name='get_article_by_id'),
]
