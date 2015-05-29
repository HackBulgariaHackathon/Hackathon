# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='number',
            field=models.CharField(max_length=8),
        ),
    ]
