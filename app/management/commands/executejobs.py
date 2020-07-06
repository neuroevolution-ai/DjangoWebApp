from django.core.management.base import BaseCommand
from app.models import Job
import logging

logger = logging.getLogger('training')


class Command(BaseCommand):
    help = 'execute jobs from jobqueue'

    def handle(self, *args, **options):
        while True:
            try:
                job = Job.objects.all()[0]
                self.__create_json_from_job(job)
                job.delete()
            except Exception as e:
                logger.error(e)
                break

    def __create_json_from_job(self, job):

        return

