from django.db import models

# Create your models here.

class Wiki(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    data_created = models.DateTimeField(auto_now_add=True)

