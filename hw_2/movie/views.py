from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def get_movies(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def get_movie_by_id(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        return JsonResponse({'id': movie.id, 'title': movie.title, 'description': movie.description,
                             'producer': movie.producer, 'duration': movie.duration})
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
