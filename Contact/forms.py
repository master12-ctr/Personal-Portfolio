from django import forms
from django.core.exceptions import ValidationError
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django_countries.fields import CountryField
from django.core.validators import MaxLengthValidator

def validate_alphabetic(value):
    if not value.replace(' ', '').isalpha():
        raise ValidationError("Field must contain only letters.")

    if value.count(' ') > 2:
        raise ValidationError("Field can have a maximum of one space.")

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        validators=[
            validate_alphabetic,
            MaxLengthValidator(25, message="Field must be at most 25 characters.")
        ],
        error_messages={'invalid': 'Field must contain only letters.'},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    country_code = CountryField(default='ET').formfield(
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_phone_number(self):
        country_code = self.cleaned_data.get('country_code')
        phone_number = self.cleaned_data.get('phone_number')

        if country_code and phone_number:
            phone_number = f'{country_code.strip()} {phone_number.strip()}'

        return phone_number

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'country_code', 'phone_number', 'attachment']