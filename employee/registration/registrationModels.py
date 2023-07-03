from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserRegistrationManager(BaseUserManager):
    def create_user(self, username, email, phonenumber, password, rec_created_time):
        user = self.model(
            username=username,
            email=email,
            phonenumber=phonenumber,
            password=password,
            rec_created_time=rec_created_time
        )
        # user.set_password(password)
        user.save()
        return user


class UserRegistration(models.Model):
    objects = UserRegistrationManager()
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    rec_created_time = models.CharField(max_length=128)

    # def set_password(self, password):
    #     self.password = make_password(password)