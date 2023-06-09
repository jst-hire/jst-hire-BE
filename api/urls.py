
#from django.conf.urls import url
from django.urls import path
from . import views
from .registration import registration

urlpatterns = [
    path('', views.home, name="home"),
    path('register', registration.Registration.as_view(), name="register"),
]