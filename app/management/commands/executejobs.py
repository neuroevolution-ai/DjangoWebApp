from django.core.management.base import BaseCommand
from app.models import Job
import logging
import json

logger = logging.getLogger('training')


# TODO: updated README.md
class Command(BaseCommand):
    help = 'executes jobs from job queue'

    def handle(self, *args, **options):
        while True:
            try:
                all_jobs = Job.objects.all()
                all_numbers = []
                for current in all_jobs:
                    all_numbers.append(current.number)
                smallest = min(all_numbers)
                job = Job.objects.filter(number=smallest)[0]
                self.__create_json_from_job(job)
                # TODO: execute job
                job.delete()
                # TODO: logs leeren?
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def __create_json_from_job(job):
        configuration = job.__dict__

        # convert decimal to float
        configuration['trainer_sigma'] = float(configuration['trainer_sigma'])
        configuration['brain_delta_t'] = float(configuration['brain_delta_t'])
        configuration['brain_clipping_range_max'] = float(configuration['brain_clipping_range_max'])
        configuration['brain_clipping_range_min'] = float(configuration['brain_clipping_range_min'])

        # nest
        configuration['trainer'] = {
            'population_size': configuration['trainer_population_size'],
            'sigma': configuration['trainer_sigma']
        }
        configuration['brain'] = {
            'number_neurons': configuration['brain_number_neurons'],
            'delta_t': configuration['brain_delta_t'],
            'optimize_state_boundaries': configuration['brain_optimize_state_boundaries'],
            'clipping_range_max': configuration['brain_clipping_range_max'],
            'clipping_range_min': configuration['brain_clipping_range_min'],
            'optimize_y0': configuration['brain_optimize_y0'],
            'set_principle_diagonal_elements_of_W_negative': configuration['brain_set_principle_diagonal_elements_of_W_negative']
        }
        configuration['episode_runner'] = {
            'keep_env_seed_fixed_during_generation': configuration['episode_runner_keep_env_seed_fixed_during_generation'],
            'number_fitness_runs': configuration['episode_runner_number_fitness_runs']
        }

        # delete unused keys
        configuration.pop('_state')
        configuration.pop('id')
        configuration.pop('number')
        configuration.pop('trainer_sigma')
        configuration.pop('trainer_population_size')
        configuration.pop('brain_number_neurons')
        configuration.pop('brain_delta_t')
        configuration.pop('brain_optimize_state_boundaries')
        configuration.pop('brain_clipping_range_max')
        configuration.pop('brain_clipping_range_min')
        configuration.pop('brain_optimize_y0')
        configuration.pop('brain_set_principle_diagonal_elements_of_W_negative')
        configuration.pop('episode_runner_keep_env_seed_fixed_during_generation')
        configuration.pop('episode_runner_number_fitness_runs')

        with open('Configuration.json', 'w') as file:
            json.dump(configuration, file)
