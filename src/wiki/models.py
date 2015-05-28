from django.db import models

# Create your models here.

class Wiki(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date_published = models.DateTimeField(auto_now_add=True)
