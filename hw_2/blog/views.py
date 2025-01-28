from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def get_articles(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def get_article_by_id(request, id):
    try:
        article = Article.objects.get(pk=id)
        return JsonResponse({'id': article.id, 'title': article.title, 'text': article.text, 'author': article.author})
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)
