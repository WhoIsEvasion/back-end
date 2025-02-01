from django.shortcuts import render
from .models import Article

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})

def get_article_by_id(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article_detail.html', {'article': article})