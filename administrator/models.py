from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


# Create your models here.

class AdminRegistrationManager(BaseUserManager):
    def create_user(self, username, email, phonenumber, password, rec_created_time):
        user = self.model(
            username=username,
            email=email,
            phonenumber=phonenumber,
            password=password,
            rec_created_time=rec_created_time
        )
        user.set_password(password)
        user.save()
        return user


class AdminRegistration(AbstractBaseUser):
    DoesNotExist = None
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    rec_created_time = models.CharField(max_length=128)

    # Add other fields as per your requirements

    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    objects = AdminRegistrationManager()
    # Other fields in your custom user model
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'

    def _str_(self):
        return  self.username
