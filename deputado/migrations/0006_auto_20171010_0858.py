# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-10 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deputado', '0005_auto_20171010_0842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
