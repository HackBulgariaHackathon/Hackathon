from django.db import models
# Create your models here.

class Paten_list(models.Model):
    user = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.user)


class Vehicle(models.Model):
    status = models.CharField(max_length=10, null=False, blank=False)
    date_reserved = models.DateTimeField()
    date_returned = models.DateTimeField()
    user_id = models.ForeignKey(Paten_list)

    def __str__(self):
        return "{} - {} - {}".format
        (self.status, self.date_reserved, self.date_returned)
