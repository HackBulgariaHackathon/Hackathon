# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0003_networkdevice_networkequipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkequipment',
            name='device_address',
        ),
        migrations.AddField(
            model_name='networkequipment',
            name='device_address',
            field=models.ManyToManyField(to='network_site.Host'),
        ),
    ]
