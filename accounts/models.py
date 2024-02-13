from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=40,null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=10)
    registertime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    donateStatus = models.BooleanField(default=False, null=True, blank=True)
    district = models.CharField(max_length = 100, null=True, blank=True)
    subdistrict = models.CharField(max_length = 100, null=True, blank=True)
    union = models.CharField(max_length = 100, null=True, blank=True)
    contract = models.CharField(max_length=11)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


