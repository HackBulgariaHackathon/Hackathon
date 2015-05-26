from django.db import models
from django.contrib.auth import Group, User

# Create your models here.

class Document(models.Model):
    uploader = models.ForeignKey(User)
    department = models.ForeignKey(Group)
    name = models.CharField(max_length=255, null=False, blank=True)
    tags = models.TextField(null=True, blank=False)
    serial = models.CharField(max_length=25)
    uploaded = models.DateTimeField()
    doc = models.FileField()
