from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author') 
    search_fields = ('title', 'content')
    list_filter = ('author',)  

admin.site.register(Article, ArticleAdmin)