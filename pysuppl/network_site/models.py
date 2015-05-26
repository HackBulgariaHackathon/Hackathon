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


class NetworkDevice(models.Model):
    device_type = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.device_type)


class NetworkEquipment(models.Model):
    device_type = models.ForeignKey(NetworkDevice)
    name = models.CharField(max_length=50)
    number_of_ports = models.PositiveSmallIntegerField()
    desctiption = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.device_type)


class Host(models.Model):
    ip_net = models.ForeignKey(Network)
    ip_addr = models.CharField(max_length=100,
                               unique=True,
                               verbose_name="IP-Addr")
    macaddr = models.CharField(max_length=30, unique=True,
                               validators=[validate_macaddr])
    device = models.ForeignKey(NetworkEquipment)
    host_name = models.CharField(max_length=50, unique=True)
    desctiption = models.TextField()

    class Meta:
        unique_together = (("device", "ip_addr"),)

    def clean(self):
        try:
            IPAddress(self.ip_addr)
        except:
            raise ValidationError('{} is not a valid IP address'.format(self.ip_addr))
        if IPAddress(self.ip_addr) not in IPNetwork(self.ip_net.ipnet):
            raise ValidationError('{} IP dont belong to subnet {}'.format(self.ip_addr, self.ip_net.ipnet))

    def __str__(self):
        return '{}'.format(self.ip_addr)


class Vlan(models.Model):
    vlan_id = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=32)
    desctiption = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.vlan_id, self.name)


class NetworkProt(models.Model):
    port_name = models.CharField(max_length=10)
    device = models.ForeignKey(NetworkEquipment)
    to_where = models.ForeignKey(Host)
    vlans = models.ManyToManyField(Vlan)
    T_STATUS = (
        (1, 'trunk'),
        (2, 'access'),
        )
    port_status = models.IntegerField(choices=T_STATUS)

    class Meta:
        unique_together = (("device", "port_name"),)

    def __str__(self):
        return '{} - {}'.format(self.port_name, self.device)

    def get_vlans(self):
        return ', '.join([str(obj.vlan_id) for obj in self.vlans.all()])

    get_vlans.short_description = 'Vlans'
