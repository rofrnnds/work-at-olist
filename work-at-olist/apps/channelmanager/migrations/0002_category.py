# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channelmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='channelmanager.Channel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='channelmanager.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
