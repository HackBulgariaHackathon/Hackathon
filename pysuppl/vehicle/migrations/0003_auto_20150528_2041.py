# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicle_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='date_reserved',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='date_returned',
        ),
        migrations.AlterField(
            model_name='paten_list',
            name='user',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(max_length=11),
        ),
    ]
