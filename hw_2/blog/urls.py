from django.urls import path
from . import views
from .views import get_articles

urlpatterns = [
    path('', views.get_articles, name='get_articles'), 
    path('<int:id>/', views.get_article_by_id, name='get_article_by_id'),  
]