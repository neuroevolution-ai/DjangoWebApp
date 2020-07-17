# Generated by Django 3.0.6 on 2020-06-09 13:40

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200609_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='brain_number_neurons',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='episode_runner_number_fitness_runs',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='number_generations',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='random_seed',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=1000, size=None),
        ),
        migrations.AlterField(
            model_name='config',
            name='trainer_population_size',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=1000, size=None),
        ),
    ]
