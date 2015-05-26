# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0002_host_desctiption'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('device_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkEquipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number_of_ports', models.PositiveSmallIntegerField()),
                ('desctiption', models.TextField()),
                ('device_address', models.ForeignKey(to='network_site.Host')),
                ('device_type', models.ForeignKey(to='network_site.NetworkDevice')),
            ],
        ),
    ]
