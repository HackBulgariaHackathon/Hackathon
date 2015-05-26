# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('serial', models.CharField(max_length=25)),
                ('date_bought', models.DateTimeField()),
                ('name', models.CharField(null=True, max_length=32, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=55)),
                ('serial', models.CharField(max_length=25)),
                ('expire', models.DateTimeField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('installed', models.ManyToManyField(to='inventory.Computer')),
                ('license_id', models.ForeignKey(to='inventory.License')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='software',
            name='vendor_id',
            field=models.ForeignKey(to='inventory.Vendor'),
        ),
        migrations.AddField(
            model_name='computer',
            name='vendor_id',
            field=models.ForeignKey(to='inventory.Vendor'),
        ),
    ]
