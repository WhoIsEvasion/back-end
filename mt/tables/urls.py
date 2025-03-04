from django.urls import path
from .views import table_list, table_create, available_tables

urlpatterns = [
    path('', table_list, name="table_list"),
    path('create/', table_create, name="table_create"),
    path('available/', available_tables, name="available_tables"),
]

