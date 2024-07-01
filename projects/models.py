from django.db import models

# Create your models here.
from Home.models import CustomUser

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    repository_link = models.URLField(max_length=255, null=True, blank=True)
    screenshot = models.ImageField(upload_to='project_screenshots')
    def __str__(self):
        return self.title