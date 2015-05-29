# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0005_auto_20150526_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkProt',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('port_name', models.CharField(max_length=10)),
                ('port_status', models.IntegerField(choices=[(1, 'trunk'), (2, 'access')])),
                ('device', models.ForeignKey(to='network_site.NetworkEquipment')),
                ('to_where', models.ForeignKey(to='network_site.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Vlans',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vlan_id', models.PositiveSmallIntegerField(unique=True)),
                ('name', models.CharField(max_length=32)),
                ('desctiption', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='networkprot',
            name='vlans',
            field=models.ManyToManyField(to='network_site.Vlans'),
        ),
        migrations.AlterUniqueTogether(
            name='networkprot',
            unique_together=set([('device', 'port_name')]),
        ),
    ]
