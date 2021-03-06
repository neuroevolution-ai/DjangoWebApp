"""praktikum_ingenieursmäßige_softwareentwicklung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import create_config, ConfigListView, JobQueue, delete_job, show_log, move_job

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_config, name="create_config"),
    path('configurations/', ConfigListView.as_view(), name="configs"),
    path('jobs/', JobQueue.as_view(), name="jobqueue"),
    path('deleteJob/<job_id>', delete_job),
    path('logs/', show_log, name="logs"),
    path('moveJob/<job_id>', move_job)
]
