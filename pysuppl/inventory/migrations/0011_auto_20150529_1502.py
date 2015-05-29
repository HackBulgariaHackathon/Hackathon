# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20150529_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(null=True, max_length=10)),
                ('firstname', models.CharField(null=True, max_length=20)),
                ('lastname', models.CharField(null=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role_id',
            field=models.ForeignKey(to='inventory.Role'),
        ),
    ]
