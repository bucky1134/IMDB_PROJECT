  
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

#user modeml serializers for serializing deafult USER model in django

class UserRegisterSerializer(serializers.ModelSerializer):

    #Not adding password and other information as a part of serialization response after successfull registration
    password = serializers.CharField(
        write_only=True
    )
    is_staff = serializers.CharField(
        write_only=True,
    )
    is_superuser = serializers.CharField(
        write_only=True,
    )
    class Meta:
        model = get_user_model()
        fields = ('username','password','email','is_superuser','is_staff')

    #creating new user instance  from serialized data
    def create(self, validated_data,instance=None):
        user = User(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
                is_staff=self.validated_data['is_staff'],
                is_superuser=self.validated_data['is_superuser']
            )
        user.set_password(self.validated_data['password'])
        user.save()
        return user
        
