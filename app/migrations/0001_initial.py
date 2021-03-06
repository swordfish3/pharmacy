# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=512)),
                ('retail', models.DecimalField(decimal_places=2, max_digits=5, max_length=50)),
                ('wholesale', models.DecimalField(decimal_places=2, max_digits=5, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
