# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-10 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deputado', '0003_links_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='destino',
            field=models.TextField(default='#'),
        ),
    ]
