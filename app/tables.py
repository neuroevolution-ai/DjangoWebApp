import django_tables2 as tables
from app.models import Config, Job


class ConfigTable(tables.Table):
    class Meta:
        model = Config
        template_name = "django_tables2/bootstrap.html"
        exclude = ('id', )


class JobQueueTable(tables.Table):
    delete = tables.TemplateColumn(
        '<form action="/deleteJob/{{record.id}}" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">delete</button></form>',
        orderable=False,
        verbose_name=''
    )

    # TODO: Felder nicht einzeln aufzählen!
    class Meta:
        model = Job
        fields = ('environment',
                  'neural_network_type',
                  'random_seed',
                  'number_generations',
                  'trainer_type',
                  'trainer_population_size',
                  'trainer_sigma',
                  'brain_number_neurons',
                  'brain_delta_t',
                  'brain_optimize_state_boundaries',
                  'brain_clipping_range_max',
                  'brain_clipping_range_min',
                  'brain_optimize_y0',
                  'brain_set_principle_diagonal_elements_of_W_negative',
                  'episode_runner_keep_env_seed_fixed_during_generation',
                  'delete')
        template_name = "django_tables2/bootstrap.html"
        orderable = False
