from django.db import models

# Create your models here.
from Home.models import CustomUser

class experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100 , default="Addis Abeba")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    def __str__(self):
        return self.position
class certificates(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_url = models.URLField(null=True, blank=True)
    image = models.FileField(upload_to='certificates_images/')
    def __str__(self):
        return self.title
class education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100 , default="Addis Abeba")
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    def __str__(self):
        return self.institution
from django.core.validators import MinValueValidator, MaxValueValidator

class skills(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.name
class languages(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.name