from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

@deconstructible
class PdfValidator(object):
    def __call__(self, value):
        if not value.name.endswith('.pdf'):
            raise ValidationError('Only PDF files are allowed.')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone_number = models.CharField(max_length=15)
    attachment = models.FileField(blank=True, null=True, validators=[PdfValidator()], upload_to='contact_messages')

    def __str__(self):
        return self.name


class Document(models.Model):
    pdf_file = models.FileField(upload_to='static/pdf/')