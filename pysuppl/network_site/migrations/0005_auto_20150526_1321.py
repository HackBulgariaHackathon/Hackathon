# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0004_auto_20150526_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkequipment',
            name='device_address',
        ),
        migrations.AddField(
            model_name='host',
            name='device',
            field=models.ForeignKey(default=1, to='network_site.NetworkEquipment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='host_name',
            field=models.CharField(max_length=50, unique=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkequipment',
            name='name',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('device', 'ip_addr')]),
        ),
    ]
