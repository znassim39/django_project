from django.shortcuts import render, get_object_or_404
from django.http import Http404
from NewApp.models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    print(articles)
    # comment 2
    return render(request, 'NewApp/accueil.html', {'articles': articles})

def showArticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.all()


    return render(request, 'NewApp/article.html', {'article': article, 'comments': comments})

def addArticle(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'NewApp/add.html', locals())

def addComment(request):

    form = CommentForm(request.POST or None)

    print(form)

<<<<<<< Updated upstream
=======
    print('ln2')

>>>>>>> Stashed changes
    if form.is_valid():
        form.save()

    return render(request, 'NewApp/addComment.html', locals())