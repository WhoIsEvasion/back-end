from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at') 
    search_fields = ('title', 'content')
    list_filter = ('created_at',)  

admin.site.register(Article, ArticleAdmin)
