from django.core.management.base import BaseCommand
from app.models import Job, Config
from random import choice
from time import sleep
import logging

logger = logging.getLogger('root')


class Command(BaseCommand):
    help = 'fills jobqueue every 10 seconds if number of jobs < 5'

    def __init__(self):
        super().__init__()
        self.seconds_to_wait = 10
        self.max_number_of_jobs = 5

    def handle(self, *args, **options):
        while True:
            try:
                self.__add_jobs()
                sleep(self.seconds_to_wait)
            except Exception as e:
                logger.error(e)
                break

    def __add_jobs(self):
        if Config.objects.count > 0:
            while Job.objects.count() < self.max_number_of_jobs:
                random_config = choice(Config.objects.all())
                job = self.__create_job_from_config(random_config)
                job.save()
        return

    def __create_job_from_config(self, config):
        job = Job()
        job.number = self.__get_number_of_last_job() + 1

        job.environment = choice(config.environment)
        job.random_seed = choice(config.random_seed)
        job.number_generations = choice(config.number_generations)
        job.use_worker_processes = config.use_worker_processes

        job.optimizer_type = choice(config.optimizer_type)
        job.optimizer_population_size = choice(config.optimizer_population_size)
        job.optimizer_sigma = choice(config.optimizer_sigma)
        job.optimizer_checkpoint_frequency = choice(config.optimizer_checkpoint_frequency)
        job.optimizer_hof_size = choice(config.optimizer_hof_size)

        job.brain_type = choice(config.brain_type)
        job.brain_number_neurons = choice(config.brain_number_neurons)
        job.brain_use_bias = config.brain_use_bias
        job.brain_delta_t = choice(config.brain_delta_t)
        job.brain_neuron_activation = choice(config.brain_neuron_activation)
        job.brain_neuron_activation_inplace = config.brain_neuron_activation_inplace
        job.brain_normalize_input = config.brain_normalize_input
        job.brain_normalize_input_target = choice(config.brain_normalize_input_target)
        job.brain_optimize_state_boundaries = choice(config.brain_optimize_state_boundaries)
        job.brain_clipping_range_max = choice(config.brain_clipping_range_max)
        job.brain_clipping_range_min = choice(config.brain_clipping_range_min)
        job.brain_optimize_y0 = config.brain_optimize_y0
        job.brain_set_principle_diagonal_elements_of_W_negative = config.brain_set_principle_diagonal_elements_of_W_negative
        job.brain_w_mask = choice(config.brain_w_mask)
        job.brain_w_mask_param = choice(config.brain_w_mask_param)
        job.brain_v_mask = choice(config.brain_v_mask)
        job.brain_v_mask_param = choice(config.brain_v_mask_param)
        job.brain_t_mask = choice(config.brain_t_mask)
        job.brain_t_mask_param = choice(config.brain_t_mask_param)
        job.brain_parameter_perturbations = choice(config.brain_parameter_perturbations)

        job.episode_runner_type = choice(config.episode_runner_type)
        job.episode_runner_keep_env_seed_fixed_during_generation = config.episode_runner_keep_env_seed_fixed_during_generation
        job.episode_runner_number_fitness_runs = choice(config.episode_runner_number_fitness_runs)
        job.episode_runner_reuse_env = config.episode_runner_reuse_env
        job.episode_runner_max_steps_per_run = choice(config.episode_runner_max_steps_per_run)
        job.episode_runner_max_steps_penalty = choice(config.episode_runner_max_steps_penalty)

        return job

    @staticmethod
    def __get_number_of_last_job():
        if Job.objects.count() > 0:
            last_job = Job.objects.last()
            return last_job.number
        else:
            return 0

