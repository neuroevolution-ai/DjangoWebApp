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

    move = tables.TemplateColumn(
        '<form action="/moveJob/{{record.id}}" method="post">{% csrf_token %}<input type="hidden" name="_method" value="move"><button type="submit" class="btn btn-primary btn-xs">move downwards</button></form>',
        orderable=False,
        verbose_name=''
    )

    class Meta:
        model = Job
        exclude = ('id', )
        template_name = "django_tables2/bootstrap.html"
