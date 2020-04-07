from django.db import models

class NewsArticle(models.Model):
    heading = models.CharField(max_length=50)
    publication_date = models.DateTimeField('date published')
    story_text = models.CharField(max_length=200)
