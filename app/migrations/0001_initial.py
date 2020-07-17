# Generated by Django 3.0.6 on 2020-06-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.CharField(max_length=200)),
                ('neural_network_type', models.CharField(max_length=200)),
                ('random_seed', models.IntegerField()),
                ('number_generations', models.IntegerField()),
                ('trainer_type', models.CharField(max_length=200)),
                ('trainer_population_size', models.IntegerField()),
                ('trainer_sigma', models.DecimalField(decimal_places=2, max_digits=5)),
                ('brain_number_neurons', models.IntegerField()),
                ('brain_delta_t', models.DecimalField(decimal_places=2, max_digits=5)),
                ('brain_optimize_state_boundaries', models.BooleanField()),
                ('brain_clipping_range_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('brain_clipping_range_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('brain_optimize_y0', models.BooleanField()),
                ('brain_set_principle_diagonal_elements_of_W_negative', models.BooleanField()),
                ('episode_runner_keep_env_seed_fixed_during_generation', models.BooleanField()),
                ('episode_runner_number_fitness_runs', models.IntegerField()),
            ],
        ),
    ]
