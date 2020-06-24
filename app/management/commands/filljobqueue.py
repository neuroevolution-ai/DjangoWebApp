from django.core.management.base import BaseCommand
from app.models import Job, Config
from random import randint, choice
from time import sleep


# TODO: Anzahl Minuten und Anzahl Jobs konfigurierbar machen
class Command(BaseCommand):
    help = 'fills jobqueue every 10 seconds if number of jobs < 5'

    def handle(self, *args, **options):
        while True:
            # TODO: try... except
            while Job.objects.count() < 5:
                random_number = randint(1, Config.objects.count())
                counter = 1
                for config in Config.objects.all():
                    if counter == random_number:
                        random_config = config
                        break
                    counter += 1
                job = create_job_from_config(random_config)
                job.save()
            sleep(10)


def create_job_from_config(config):
    job = Job()
    job.environment = random_element_of_list(config.environment)
    job.neural_network_type = random_element_of_list(config.neural_network_type)
    job.random_seed = random_element_of_list(config.random_seed)
    job.number_generations = random_element_of_list(config.number_generations)
    job.trainer_type = random_element_of_list(config.trainer_type)
    job.trainer_population_size = random_element_of_list(config.trainer_population_size)
    job.trainer_sigma = float(random_element_of_list(config.trainer_sigma))
    job.brain_number_neurons = random_element_of_list(config.brain_number_neurons)
    job.brain_delta_t = float(random_element_of_list(config.brain_delta_t))
    job.brain_optimize_state_boundaries = config.brain_optimize_state_boundaries
    job.brain_clipping_range_max = float(random_element_of_list(config.brain_clipping_range_max))
    job.brain_clipping_range_min = float(random_element_of_list(config.brain_clipping_range_min))
    job.brain_optimize_y0 = config.brain_optimize_y0
    job.brain_set_principle_diagonal_elements_of_W_negative = config.brain_set_principle_diagonal_elements_of_W_negative
    job.episode_runner_keep_env_seed_fixed_during_generation = config.episode_runner_keep_env_seed_fixed_during_generation
    job.episode_runner_number_fitness_runs = random_element_of_list(config.episode_runner_number_fitness_runs)
    return job


def random_element_of_list(list_of_elements):
    size = len(list_of_elements)
    random_number = randint(0, size - 1)
    return list_of_elements[random_number]
