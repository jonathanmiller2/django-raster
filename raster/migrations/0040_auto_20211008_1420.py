# Generated by Django 3.2.4 on 2021-10-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0039_auto_20190313_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='RasterProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='rasterlayer',
            name='day',
            field=models.IntegerField(default=1, help_text='A value from 0 to 364 indicating what day of the year the data is from.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rasterlayer',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rasterlayer',
            name='year',
            field=models.IntegerField(default=1, help_text='The 4 digit year the data is from.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='legendentry',
            name='code',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='legendsemantics',
            name='keyword',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='nodata',
            field=models.CharField(blank=True, help_text='Leave blank to keep the internal band nodata values. If a nodata value is specified here, it will be used for all bands of this raster.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rasterlayer',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='raster.rasterproduct'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='rasterlayer',
            unique_together={('product', 'year', 'day')},
        ),
        migrations.RemoveField(
            model_name='rasterlayer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='rasterlayer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rasterlayer',
            name='rasterfile',
        ),
        migrations.RemoveField(
            model_name='rasterlayer',
            name='source_url',
        ),
    ]
