from django.core.management.base import BaseCommand
from app.models import Job, Config
from random import choice
from time import sleep


# TODO: Anzahl Minuten und Anzahl Jobs konfigurierbar machen
class Command(BaseCommand):
    help = 'fills jobqueue every 10 seconds if number of jobs < 5'

    def handle(self, *args, **options):
        while True:
            try:
                while Job.objects.count() < 5:
                    random_config = choice(Config.objects.all())
                    job = self.__create_job_from_config(random_config)
                    job.save()
                sleep(10)
            except Exception as e:
                print(e) # TODO: logfile oder ähnliches
                break

    @staticmethod
    def __create_job_from_config(config):
        job = Job()
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
