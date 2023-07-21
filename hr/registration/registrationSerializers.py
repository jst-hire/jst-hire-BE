from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phonenumber = serializers.CharField(max_length=20)
    company_name = serializers.CharField(max_length=20)
    location = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128)
    confirmpassword = serializers.CharField(max_length=128)
    # rec_created_time =