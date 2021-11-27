# -*- coding: utf-8 -*-
# Generated by Django 1.11.2.dev20170508150049 on 2017-05-09 05:48
from django.db import migrations


def set_legend_on_entry(apps, schema_editor):
    # Get models.
    Legend = apps.get_model("raster", "Legend")
    LegendEntryOrder = apps.get_model("raster", "LegendEntryOrder")
    # Loop through legend and entries.
    for legend in Legend.objects.all():
        for entry in legend.entries.all():
            # Set legend direct foreign key.
            entry.legend = legend
            # Update legend entry order field from related table if it exists.
            # The related table has a unique constraint, so there are no
            # duplicates here. Getting the first instance is sufficient.
            order = LegendEntryOrder.objects.filter(legend=legend, legendentry=entry).first()
            if order:
                entry.code = order.code
            # Save updated entry.
            entry.save()


def run_backwards(apps, schema_editor):
    # The backward migration does not have to do anythign, the data
    # is copied to the new fields but not removed. The data gets removed
    # in the subsequent migration where the entry through table is dropped.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0035_auto_20170509_0545'),
    ]

    operations = [
        migrations.RunPython(set_legend_on_entry, run_backwards),
    ]
