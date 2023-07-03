import sys
import traceback
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from employee.login.loginSerializers import LoginSerializer
from employee.registration.registrationModels import UserRegistration
# Import your UserProfile model or any other model representing the additional user data


class Login(generics.GenericAPIView):
    permission_classes = ()

    def __init__(self):
        # logger.info("Registration API Service Started")
        print("Login API Service Started")

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            print(">>>>", email, password)
            user = authenticate(request, username=email, password=password)
            print(">>>>", user)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': 'User logged in successfully'})
            else:
                return JsonResponse({'error': 'Invalid credentials'})

        except ValueError:
            return HttpResponse("registration")
        except Exception as err:
            http_err = traceback.format_exc()
            # data = sys.exc_info()[1]
            print(http_err)
            # return HttpResponse(json.dumps({"error": http_err}))
            return HttpResponse(err)
