# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='naprava',
        ),
    ]
