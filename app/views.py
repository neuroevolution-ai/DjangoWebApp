from django.shortcuts import render
from app.forms import ConfigForm
from django.http import HttpResponseRedirect, HttpResponse
from django_tables2 import SingleTableView
from app.models import Config, Job
from app.tables import ConfigTable, JobQueueTable

# Create your views here.


def create_config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ConfigForm()
    return render(request, 'form.html', {'form': form})


class ConfigListView(SingleTableView):
    model = Config
    table_class = ConfigTable
    template_name ="configListView.html"


def delete_job(request, job_id=1):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id=job_id)
        except: # TODO: except job does not exist
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
