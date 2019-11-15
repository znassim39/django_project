from django.urls import path

from . import views

app_name = 'NewApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>', views.showArticle, name='article'),
    path('add', views.addArticle, name='add'),
    path('addComment', views.addComment, name='addComment'),
]