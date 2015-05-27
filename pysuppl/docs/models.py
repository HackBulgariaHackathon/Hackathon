# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Document(models.Model):

    """ Table documents where we save info
        about uploaded documents """

    uploader = models.ForeignKey(User)
    department = models.ForeignKey(Group)
    name = models.CharField(max_length=255, null=False, blank=True)
    tags = models.TextField(null=True, blank=False)
    serial = models.CharField(max_length=25)
    uploaded = models.DateTimeField()
    doc = models.FileField()
