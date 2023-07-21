import sys
import traceback
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from hr.login.loginSerializers import LoginSerializer
from hr.models import hrRegistration
# Import your UserProfile model or any other model representing the additional user data


class Login(generics.GenericAPIView):
    permission_classes = ()

    def __init__(self):
        # logger.info("Registration API Service Started")
        print("Login API Service Started")

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request):
        if request.method == 'POST':
            # Get the login credentials from the request
            email = request.data['email']
            password = request.data['password']
            try:
                # Get the user object with the provided username
                user = hrRegistration.objects.get(email=email)
            except hrRegistration.DoesNotExist:
                # If the user does not exist, return an error response
                return JsonResponse({'error': 'Invalid username or password'})
            # Use the check_password function to compare the provided password with the encrypted one
            if check_password(password, user.password):
                # Passwords match, login successful
                return JsonResponse({'message': 'Login successful'})
            else:
                # Passwords do not match, login failed
                return JsonResponse({'error': 'Invalid username or password'})

        return JsonResponse({'error': 'Invalid request method'})

