from django.db import models

# Create your models here.
class comment(models.Model):
    text=models.TextField()
    author=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
