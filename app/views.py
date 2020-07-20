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
            job, method, data = get_job_method_and_data(request, job_id)
        except Job.DoesNotExist:
            return HttpResponse(status=404)
        if method == 'delete':
            job.delete()
            return HttpResponseRedirect('/jobs')


def get_job_method_and_data(request, job_id):
    job = Job.objects.get(id=job_id)
    data = request.POST
    method = data.get('_method', '').lower()
    return job, method, data


def move_job(request, job_id):
    if request.method == 'POST':
        try:
            job, method, data = get_job_method_and_data(request, job_id)
        except Job.DoesNotExist:
            return HttpResponse(status=404)
        if method == 'move':
            number = job.number
            all_jobs = Job.objects.all()

            all_numbers = []
            for current_job in all_jobs:
                all_numbers.append(current_job.number)

            numbers_greater_than_number = [n for n in all_numbers if n > number]
            smallest = min(numbers_greater_than_number)

            Job.objects.filter(number=smallest).update(number=number)
            Job.objects.filter(id=job_id).update(number=smallest)

            return HttpResponseRedirect('/jobs/?sort=number')


def get_key(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key


class JobQueue(SingleTableView):
    model = Job
    table_class = JobQueueTable
    template_name = "jobQueue.html"


def show_log(request):
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'training.log')
    file = open(path)
    lines = file.readlines()
    file.close()
    return render(request, 'logs.html', {'lines': lines})
