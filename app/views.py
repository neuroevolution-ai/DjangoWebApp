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


# TODO: DRY (s.o.)
def move_job(request, job_id):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return HttpResponse(status=404)
        data = request.POST
        method = data.get('_method', '').lower()
        if method == 'move':
            number = job.number
            all_jobs = Job.objects.all()

            all_numbers = []
            for current_job in all_jobs:
                all_numbers.append(current_job.number)

            # TODO: was, wenn numbers_greater_than_number == []?
            numbers_greater_than_number = [n for n in all_numbers if n > number]
            smallest = min(numbers_greater_than_number)

            Job.objects.filter(number=smallest).update(number=number)
            Job.objects.filter(id=job_id).update(number=smallest)

            return HttpResponseRedirect('/jobs')


def get_key(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key


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
