from django.shortcuts import render
from .models import Programminglanguages

def welcome(request):
    projects = Programminglanguages.objects.all()
    context = {'projects': projects}
    return render(request, 'projectapp/projects.html', context)

def project(request, pk):
    project = Programminglanguages.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projectapp/single-project.html', context)
