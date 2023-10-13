from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    published_date = models.DateField()
    ratings = models.IntegerField()