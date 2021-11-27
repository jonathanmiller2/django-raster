# -*- coding: utf-8 -*-
# Generated by Django 1.11.2.dev20170508150049 on 2017-05-09 05:45
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0034_legendentryorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='legendentry',
            name='code',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='legendentry',
            name='legend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='raster.Legend'),
        ),
        migrations.AlterField(
            model_name='legend',
            name='entries',
            field=models.ManyToManyField(related_name='legentries', through='raster.LegendEntryOrder', to='raster.LegendEntry'),
        ),
    ]
