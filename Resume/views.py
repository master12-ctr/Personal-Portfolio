from django.shortcuts import render

# Create your views here.

from .models import experience ,certificates, education, skills, languages

from django.http import FileResponse
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import experienceForm, certificatesForm, educationForm, skillsForm, languagesForm

def resume(request):
     all_certificates = certificates.objects.all()
     all_experience = experience.objects.all()
     all_education = education.objects.all()
     all_skills = skills.objects.all()
     all_languages=languages.objects.all()

     return render(request, 'Resume/index.html', {'all_experience': all_experience, 'all_certificates': all_certificates, 'all_education': all_education, 'all_skills': all_skills , 'all_languages':all_languages})


def download_pdf(request, filename):
    print(filename)
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf', filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf:
            response = FileResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    
    return HttpResponseNotFound("The requested PDF file was not found.")


def experience_list(request):
    experience = experience.objects.all()
    return render(request, 'experience/experience_list.html', {'experience': experience})

from .models import certificates

def certificates_list(request):
    all_certificates = certificates.objects.all()
    return render(request, 'certificates/certificates_list.html', {'certificates': all_certificates})

from .models import education

def education_list(request):
    education = education.objects.all()
    return render(request, 'education/education_list.html', {'education': education})

from .models import skills

def skills_list(request):
    skills = Skills.objects.all()
    return render(request, 'skills/skills_list.html', {'skills': skills})

@login_required
def create_experience(request):
    if request.method == 'POST':
        form = experienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user  # Assign the current user to the experience
            experience.save()
            return render(request, 'Resume/addExperience.html', {'form': form})
        

    else:
        form = experienceForm()
    return render(request, 'Resume/addExperience.html', {'form': form})

@login_required
def create_certificates(request):
    if request.method == 'POST':
        form = certificatesForm(request.POST, request.FILES)
        if form.is_valid():
            certificates = form.save(commit=False)
            certificates.user = request.user  # Assign the current user to the experience
            certificates.save()
            return render(request, 'Resume/addCertificates.html', {'form': form})
        

    else:
        form = certificatesForm()
    return render(request, 'Resume/addCertificates.html', {'form': form})

@login_required
def create_education(request):
    if request.method == 'POST':
        form = educationForm(request.POST, request.FILES)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user  # Assign the current user to the experience
            education.save()
            return render(request, 'Resume/addEducation.html', {'form': form})
        

    else:
        form = educationForm()
    return render(request, 'Resume/addEducation.html', {'form': form})

@login_required
def create_skills(request):
    if request.method == 'POST':
        form = skillsForm(request.POST, request.FILES)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.user = request.user  # Assign the current user to the experience
            skills.save()
            return render(request, 'Resume/addSkills.html', {'form': form})
        
    else:
        form = skillsForm()
    return render(request, 'Resume/addSkills.html', {'form': form})

@login_required
def create_languages(request):
    if request.method == 'POST':
        form = languagesForm(request.POST, request.FILES)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.user = request.user  # Assign the current user to the experience
            skills.save()
            return render(request, 'Resume/addLanguages.html', {'form': form})
        
    else:
        form = languagesForm()
    return render(request, 'Resume/addLanguages.html', {'form': form})

def Cdetail_view(request, cer_id):
 certificate = certificates.objects.get(id=cer_id)
 return render(request, 'Resume/Cdetail_view.html', {'certificate': certificate})