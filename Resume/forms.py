from django import forms
from .models import experience, certificates, education, skills, languages

class experienceForm(forms.ModelForm):
    class Meta:
        model = experience
        fields = ['company', 'position','location', 'start_date', 'end_date', 'description' ]

class certificatesForm(forms.ModelForm):
    class Meta:
        model = certificates
        fields = ['title', 'description','issuing_organization', 'issue_date', 'credential_url', 'image' ]

class educationForm(forms.ModelForm):
    class Meta:
        model = education
        fields = [ 'institution','degree', 'start_date', 'end_date', 'description' ]

class skillsForm(forms.ModelForm):
    class Meta:
        model = skills
        fields = [ 'name','proficiency_level', ]

class languagesForm(forms.ModelForm):
    class Meta:
        model = languages
        fields = [ 'name','proficiency_level', ]