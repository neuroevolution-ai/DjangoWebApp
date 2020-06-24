from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Config(models.Model):
    environment = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    neural_network_type = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    random_seed = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    number_generations = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    trainer_type = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    trainer_population_size = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    trainer_sigma = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_number_neurons = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_delta_t = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_optimize_state_boundaries = models.BooleanField()
    brain_clipping_range_max = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_clipping_range_min = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_optimize_y0 = models.BooleanField()
    brain_set_principle_diagonal_elements_of_W_negative = models.BooleanField()
    episode_runner_keep_env_seed_fixed_during_generation = models.BooleanField()
    episode_runner_number_fitness_runs = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))


class Job(models.Model):
    environment = models.CharField(max_length=100)
    neural_network_type = models.CharField(max_length=100)
    random_seed = models.IntegerField()
    number_generations = models.IntegerField()
    trainer_type = models.CharField(max_length=100)
    trainer_population_size = models.IntegerField()
    trainer_sigma = models.DecimalField(decimal_places=2, max_digits=5)
    brain_number_neurons = models.IntegerField()
    brain_delta_t = models.DecimalField(decimal_places=2, max_digits=5)
    brain_optimize_state_boundaries = models.BooleanField()
    brain_clipping_range_max = models.DecimalField(decimal_places=2, max_digits=5)
    brain_clipping_range_min = models.DecimalField(decimal_places=2, max_digits=5)
    brain_optimize_y0 = models.BooleanField()
    brain_set_principle_diagonal_elements_of_W_negative = models.BooleanField()
    episode_runner_keep_env_seed_fixed_during_generation = models.BooleanField()
    episode_runner_number_fitness_runs = models.IntegerField()
