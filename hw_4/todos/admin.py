from django.contrib import admin
from .models import TodoList, Todo

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description') 
    search_fields = ('title',) 
    list_filter = ('id',) 

@admin.register(Todo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'todo_list', 'due_date', 'status')
    search_fields = ('title',)
    list_filter = ('due_date', 'status')