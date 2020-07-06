from django.shortcuts import render
from app.forms import ConfigForm
from django.http import HttpResponseRedirect, HttpResponse
from django_tables2 import SingleTableView
from app.models import Config, Job
from app.tables import ConfigTable, JobQueueTable
import os

# Create your views here.


def create_config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/configurations')
    else:
        form = ConfigForm()
    return render(request, 'createConfig.html', {'form': form})


class ConfigListView(SingleTableView):
    model = Config
    table_class = ConfigTable
    template_name ="configListView.html"


def delete_job(request, job_id):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return HttpResponse(status=404)
        data = request.POST
        method = data.get('_method', '').lower()
        if method == 'delete':
            job.delete()
            return HttpResponseRedirect('/jobs')


class JobQueue(SingleTableView):
    model = Job
    table_class = JobQueueTable
    template_name = "jobQueue.html"


# TODO: Umlaute werden nicht korrekt angezeigt. Relevant?
# TODO: lines vielleicht falsch herum auflisten? -> Neuste immer oben
# TODO: lines nach gewisser Zeit löschen, damit Logfile nicht zu groß wird?
def show_log(request):
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'training.log')
    file = open(path)
    lines = file.readlines()
    file.close()
    return render(request, 'logs.html', {'lines': lines})
