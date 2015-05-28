# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paten_list',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('status', models.CharField(max_length=10)),
                ('date_reserved', models.DateTimeField()),
                ('date_returned', models.DateTimeField()),
                ('user_id', models.ForeignKey(to='vehicle.Paten_list')),
            ],
        ),
    ]
