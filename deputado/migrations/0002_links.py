# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-10 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deputado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_1', models.CharField(max_length=50)),
            ],
        ),
    ]
