# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170510_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pid',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='retail',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=100, primary_key='true', serialize=False),
        ),
    ]
