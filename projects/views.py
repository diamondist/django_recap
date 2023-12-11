from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})
