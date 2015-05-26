from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name +' ' + self.email

class License(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=55)
    serial = models.CharField(max_length=25, null=False, blank=False)
    expire = models.DateTimeField()
    comments = models.TextField()

    def __str__(self):
        return self.name


class Computer(models.Model):
    vendor_id = models.ForeignKey(Vendor)
    serial = models.CharField(max_length=25, null=False, blank=False)
    date_bought = models.DateTimeField()
    name = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name


class Software(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    vendor_id = models.ForeignKey(Vendor)
    license_id = models.ForeignKey(License)
    installed = models.ManyToManyField(Computer)

    def __str__(self):
        return "{}".format(self.name)
