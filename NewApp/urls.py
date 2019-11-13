from django.urls import path

from . import views

app_name = 'NewApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>', views.showArticle, name='article'),
]