# Generated by Django 3.0.6 on 2020-06-22 08:22

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='brain_clipping_range_max',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='brain_clipping_range_min',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='brain_delta_t',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='trainer_sigma',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=None),
        ),
    ]
