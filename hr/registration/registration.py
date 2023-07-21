import os
import json
import hashlib
import re
import sys
import traceback
from datetime import datetime
from django.http import HttpResponse
from JSTHIRE import settings
from rest_framework import generics
from api.registration import registration_queries as qry
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from hr.models import hrRegistration
from hr.registration.registrationSerializers import RegistrationSerializer
from django.db import models


class Registration(generics.GenericAPIView):
    permission_classes = ()

    def __init__(self):
        # logger.info("Registration API Service Started")
        print("Registration API Service Started")

    def get_serializer_class(self):
        return RegistrationSerializer

    def post(self, request):
        try:
            username = request.data['username']
            email = request.data['email']
            phonenumber = request.data['phonenumber']
            company_name = request.data['company_name']
            location = request.data['location']
            password = request.data['password']
            confirmpassword = request.data['confirmpassword']

            rec_cre_ts = datetime.now()

            if not username or not email or not phonenumber or not company_name or not location or not password or not confirmpassword:
                return JsonResponse({'error': 'All fields are required'})

            if password != confirmpassword:
                return JsonResponse({'error': 'Passwords do not match'})

            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return JsonResponse({'error': 'Invalid email address. Please enter the email in @ format'})

                # Check if the email is already registered
            if hrRegistration.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already registered'})
            else:
                registration = hrRegistration.objects.create_user(username=username, email=email,
                                                                  phonenumber=phonenumber, company_name=company_name,
                                                                  location=location, password=password,
                                                                  rec_created_time=rec_cre_ts)
                registration.save()
                return JsonResponse({'message': 'HR Registration was successful'})
            # return HttpResponse(json.dumps(registration))

        except ValueError:
            return HttpResponse(registration)
        except Exception as err:
            http_err = traceback.format_exc()
            data = sys.exc_info()[1]
            print(http_err)
            # return HttpResponse(json.dumps({"error": http_err}))
            return HttpResponse(err)
