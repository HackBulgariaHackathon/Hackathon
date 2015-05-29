from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vehicle(models.Model):
    status = models.CharField(max_length=11, null=False, blank=False)
    user_id = models.ForeignKey(User)
    number = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return "{} -- {} -- {}".format(self.number, self.status, self.user_id)
