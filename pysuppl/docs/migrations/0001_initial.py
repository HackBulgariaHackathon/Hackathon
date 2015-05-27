# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('tags', models.TextField(null=True)),
                ('serial', models.CharField(max_length=25)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('doc', models.FileField(upload_to='')),
                ('department', models.ForeignKey(to='auth.Group')),
                ('uploader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
