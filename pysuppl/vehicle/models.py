from django.db import models
# Create your models here.


class Paten_list(models.Model):
    user = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return "{}".format(self.user)


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=11, null=False, blank=False)
    user_id = models.ForeignKey(Paten_list)
    number = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return "{} -- {} -- {}".format(self.number, self.status, self.user_id)
