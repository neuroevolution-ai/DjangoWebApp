from django.core.management.base import BaseCommand
from app.models import Job
import logging
import json

logger = logging.getLogger('training')


# TODO: update README.md
class Command(BaseCommand):
    help = 'executes jobs from job queue'

    def handle(self, *args, **options):
        while True:
            try:
                all_jobs = Job.objects.all()
                if len(all_jobs) > 0:
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
        configuration = dict()
        configuration['environment'] = job.environment
        configuration['random_seed'] = job.random_seed
        configuration['number_generations'] = job.number_generations
        configuration['use_worker_processes'] = job.use_worker_processes
        configuration['optimizer'] = {
            'type': job.optimizer_type,
            'population_size': job.optimizer_population_size,
            'sigma': float(job.optimizer_sigma),
            'checkpoint_frequency': job.optimizer_checkpoint_frequency,
            'hof_size': job.optimizer_hof_size
        }
        configuration['brain'] = {
            'type': job.brain_type,
            'number_neurons': job.brain_number_neurons,
            'use_bias': job.brain_use_bias,
            'delta_t': float(job.brain_delta_t),
            'neuron_activation': job.brain_neuron_activation,
            'neuron_activation_inplace': job.brain_neuron_activation_inplace,
            'normalize_input': job.brain_normalize_input,
            'normalize_input_target': job.brain_normalize_input_target,
            'optimize_state_boundaries': job.brain_optimize_state_boundaries,
            'clipping_range_max': float(job.brain_clipping_range_max),
            'clipping_range_min': float(job.brain_clipping_range_min),
            'optimize_y0': job.brain_optimize_y0,
            'set_principle_diagonal_elements_of_W_negative': job.brain_set_principle_diagonal_elements_of_W_negative,
            'w_mask': job.brain_w_mask,
            'w_mask_param': job.brain_w_mask_param,
            'v_mask': job.brain_v_mask,
            'v_mask_param': job.brain_v_mask_param,
            't_mask': job.brain_t_mask,
            't_mask_param': job.brain_t_mask_param,
            'parameter_perturbations': float(job.brain_parameter_perturbations)
        }

        configuration['episode_runner'] = {
            'type': job.episode_runner_type,
            'keep_env_seed_fixed_during_generation': job.episode_runner_keep_env_seed_fixed_during_generation,
            'number_fitness_runs': job.episode_runner_number_fitness_runs,
            'reuse_env': job.episode_runner_reuse_env,
            'max_steps_per_run': job.episode_runner_max_steps_per_run,
            'max_steps_penalty': job.episode_runner_max_steps_penalty
        }

        with open('Configuration.json', 'w') as file:
            json.dump(configuration, file)
