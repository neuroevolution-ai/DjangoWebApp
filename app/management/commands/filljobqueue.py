from django.core.management.base import BaseCommand
from app.models import Job, Config
from random import choice
from time import sleep
import logging

logger = logging.getLogger('root')


# TODO: Anzahl Minuten und Anzahl Jobs konfigurierbar machen
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
        while Job.objects.count() < self.max_number_of_jobs:
            random_config = choice(Config.objects.all()) # TODO: was, wenn es noch keine Configurations gibt?
            job = self.__create_job_from_config(random_config)
            job.save()
        return

    def __create_job_from_config(self, config):
        job = Job()
        job.number = self.__get_number_of_last_job() + 1
        job.environment = choice(config.environment)
        job.neural_network_type = choice(config.neural_network_type)
        job.random_seed = choice(config.random_seed)
        job.number_generations = choice(config.number_generations)
        job.trainer_type = choice(config.trainer_type)
        job.trainer_population_size = choice(config.trainer_population_size)
        job.trainer_sigma = float(choice(config.trainer_sigma))
        job.brain_number_neurons = choice(config.brain_number_neurons)
        job.brain_delta_t = float(choice(config.brain_delta_t))
        job.brain_optimize_state_boundaries = config.brain_optimize_state_boundaries
        job.brain_clipping_range_max = float(choice(config.brain_clipping_range_max))
        job.brain_clipping_range_min = float(choice(config.brain_clipping_range_min))
        job.brain_optimize_y0 = config.brain_optimize_y0
        job.brain_set_principle_diagonal_elements_of_W_negative = config.brain_set_principle_diagonal_elements_of_W_negative
        job.episode_runner_keep_env_seed_fixed_during_generation = config.episode_runner_keep_env_seed_fixed_during_generation
        job.episode_runner_number_fitness_runs = choice(config.episode_runner_number_fitness_runs)
        return job

    @staticmethod
    def __get_number_of_last_job():
        if Job.objects.count() > 0:
            last_job = Job.objects.last()
            return last_job.number
        else:
            return 0

