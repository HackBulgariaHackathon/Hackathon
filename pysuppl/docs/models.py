from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Document(models.Model):

    uploader = models.ForeignKey(User)
    name = models.CharField(max_length=255, null=False, blank=True)
    tags = models.TextField(null=True, blank=False)
    serial = models.CharField(max_length=25)
    uploaded = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="files")

    def __uicode__(self):
        return self.name

    def __str__(self):
        return self.name
