# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
