from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies_used', 'start_date', 'end_date', 'link', 'repository_link', 'screenshot']
