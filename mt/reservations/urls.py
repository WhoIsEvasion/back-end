from django.urls import path
from .views import reservation_create, reservation_detail, user_reservations, reservation_update, reservation_delete

urlpatterns = [
    path("create/", reservation_create, name="reservation_create"),
    path('<int:id>/', reservation_detail, name="reservation_detail"),
    path('user/<int:user_id>', user_reservations, name="user_reservations"),
    path('<int:id>/update/', reservation_update, name="reservation_update"),
    path('<int:id>/delete/', reservation_delete, name="reservation_delete"),
]