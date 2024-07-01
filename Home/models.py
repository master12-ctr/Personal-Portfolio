from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser): 
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField()
    website_link = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.username
