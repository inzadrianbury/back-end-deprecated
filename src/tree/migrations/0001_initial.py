# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('parent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree.Tree')),
            ],
        ),
    ]
