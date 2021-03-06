# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 16:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naprava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeNaprave', models.CharField(default='', max_length=60)),
                ('opis', models.TextField()),
                ('cena', models.IntegerField()),
                ('picture', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
