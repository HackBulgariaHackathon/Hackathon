# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.CharField(max_length=10, null=False, blank=False)),
                ('date_reserved', models.DateTimeField()),
                ('date_returned', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='Vehicle',
            name='user_id',
            field=models.ForeignKey(to='vehicles.Paten_list'),
        ),
    ]
