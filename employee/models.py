from django.db import models


# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    rec_created_time = models.CharField(max_length=128)
