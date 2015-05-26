from django.db import models
from django.core.exceptions import ValidationError
from netaddr import *


def validate_network(value):
    try:
        IPNetwork(value)
    except:
        raise ValidationError('%s is not network address' % value)


def validate_macaddr(value):
    try:
        EUI(value, dialect=mac_unix)
    except:
        raise ValidationError('%s is not valid MAC address' % value)


class Network(models.Model):
    ipnet = models.CharField(max_length=100,
                             unique=True,
                             verbose_name="IP-Network",
                             validators=[validate_network])
    is_root = models.BooleanField()
    desctiption = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.ipnet, self.desctiption)


class Host(models.Model):
    ip_net = models.ForeignKey(Network)
    ip_addr = models.CharField(max_length=100,
                               unique=True,
                               verbose_name="IP-Addr")
    macaddr = models.CharField(max_length=30, unique=True,
                               validators=[validate_macaddr])

    def clean(self):
        try:
            IPAddress(self.ip_addr)
        except:
            raise ValidationError('{} is not a valid IP address'.format(self.ip_addr))
        if IPAddress(self.ip_addr) not in IPNetwork(self.ip_net.ipnet):
            raise ValidationError('{} IP dont belong to subnet {}'.format(self.ip_addr, self.ip_net.ipnet))
