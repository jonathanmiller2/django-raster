# Generated by Django 3.2.5 on 2021-12-24 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0040_auto_20211008_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rasterlayer',
            name='legend',
        ),
        migrations.AddField(
            model_name='rasterproduct',
            name='legend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='raster.legend'),
        ),
    ]
