from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Config(models.Model):
    environment = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    random_seed = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    number_generations = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    use_worker_processes = models.BooleanField()

    optimizer_type = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    optimizer_population_size = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    optimizer_sigma = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    optimizer_checkpoint_frequency = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    optimizer_hof_size = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))

    brain_type = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_number_neurons = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_use_bias = models.BooleanField()
    brain_delta_t = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_neuron_activation = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_neuron_activation_inplace = models.BooleanField()
    brain_normalize_input = models.BooleanField()
    brain_normalize_input_target = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_optimize_state_boundaries = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_clipping_range_max = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_clipping_range_min = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal
    brain_optimize_y0 = models.BooleanField()
    brain_set_principle_diagonal_elements_of_W_negative = models.BooleanField()
    brain_w_mask = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_w_mask_param = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_v_mask = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_v_mask_param = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_t_mask = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    brain_t_mask_param = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    brain_parameter_perturbations = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100)) #decimal

    episode_runner_type = ListCharField(base_field=models.CharField(max_length=100), max_length=(10 * 100))
    episode_runner_keep_env_seed_fixed_during_generation = models.BooleanField()
    episode_runner_number_fitness_runs = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    episode_runner_reuse_env = models.BooleanField()
    episode_runner_max_steps_per_run = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))
    episode_runner_max_steps_penalty = ListCharField(base_field=models.IntegerField(), max_length=(10 * 100))


class Job(models.Model):
    number = models.IntegerField()

    environment = models.CharField(max_length=100)
    random_seed = models.IntegerField()
    number_generations = models.IntegerField()
    use_worker_processes = models.BooleanField()

    optimizer_type = models.CharField(max_length=100)
    optimizer_population_size = models.IntegerField()
    optimizer_sigma = models.DecimalField(decimal_places=3, max_digits=5)
    optimizer_checkpoint_frequency = models.IntegerField()
    optimizer_hof_size = models.IntegerField()

    brain_type = models.CharField(max_length=100)
    brain_number_neurons = models.IntegerField()
    brain_use_bias = models.BooleanField()
    brain_delta_t = models.DecimalField(decimal_places=3, max_digits=5)
    brain_neuron_activation = models.CharField(max_length=100)
    brain_neuron_activation_inplace = models.BooleanField()
    brain_normalize_input = models.BooleanField()
    brain_normalize_input_target = models.IntegerField()
    brain_optimize_state_boundaries = models.CharField(max_length=100)
    brain_clipping_range_max = models.DecimalField(decimal_places=3, max_digits=5)
    brain_clipping_range_min = models.DecimalField(decimal_places=3, max_digits=5)
    brain_optimize_y0 = models.BooleanField()
    brain_set_principle_diagonal_elements_of_W_negative = models.BooleanField()
    brain_w_mask = models.CharField(max_length=100)
    brain_w_mask_param = models.IntegerField()
    brain_v_mask = models.CharField(max_length=100)
    brain_v_mask_param = models.IntegerField()
    brain_t_mask = models.CharField(max_length=100)
    brain_t_mask_param = models.IntegerField()
    brain_parameter_perturbations = models.DecimalField(decimal_places=3, max_digits=5)

    episode_runner_type = models.CharField(max_length=100)
    episode_runner_keep_env_seed_fixed_during_generation = models.BooleanField()
    episode_runner_number_fitness_runs = models.IntegerField()
    episode_runner_reuse_env = models.BooleanField()
    episode_runner_max_steps_per_run = models.IntegerField()
    episode_runner_max_steps_penalty = models.IntegerField()

