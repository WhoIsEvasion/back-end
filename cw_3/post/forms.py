from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description']  
        labels = {
            'name': 'Название треда',
            'description': 'Описание',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']
        labels = {
            'title': 'Заголовок',
            'content': 'Текст поста',
            'author': 'Автор',
        }