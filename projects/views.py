from django.shortcuts import render, redirect

# Create your views here.

from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Assign the current user to the project
            project.save()
            return redirect(reverse('project_detail', args=[project.id]))
        

    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})