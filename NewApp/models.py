from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    body = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="publishing date")

    class Meta:
        verbose_name = 'article'
        ordering = ['date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    body = models.TextField
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['date']
