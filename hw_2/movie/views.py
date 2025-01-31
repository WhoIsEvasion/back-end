from django.shortcuts import render
from .models import Movie

def get_movies(request):
    movies = Movie.objects.all() 
    return render(request, 'movie/movies_list.html', {'movies': movies})

def get_movie_by_id(request, id):
    try:
        movie = Movie.objects.get(id=id)
        return render(request, 'movie/movie_detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        return render(request, 'movie/movie_not_found.html')


