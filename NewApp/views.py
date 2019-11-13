from django.shortcuts import render
from django.http import Http404
from NewApp.models import Article, Comment

def index(request):
    articles = Article.objects.all()
    return render(request, 'NewApp/accueil.html', {'articles': articles})

def showArticle(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    return render(request, 'NewApp/article.html', {'article': article, 'comments': comments})
