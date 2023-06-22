#from django.conf.urls import url
from django.urls import path
from . import views
from .registration.registration import Registration

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', Registration.as_view(), name="registration"),
]