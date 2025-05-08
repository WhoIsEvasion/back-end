from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListCreateView, post_list, post_detail, PostViewSet


router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns = [
    # API маршруты
    path('', include(router.urls)),
    path('api/posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),

    # HTML-страницы
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
]
