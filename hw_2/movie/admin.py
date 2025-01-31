from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'producer', 'duration') 
    search_fields = ('title', 'producer')
    list_filter = ('title',)  

admin.site.register(Movie, MovieAdmin)