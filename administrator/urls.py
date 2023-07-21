#from django.conf.urls import url
from django.urls import path
from . import views
from .registration.registration import Registration
from .login.login import Login
urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', Registration.as_view(), name="registration"),
    path('login/', Login.as_view(), name="login"),
]