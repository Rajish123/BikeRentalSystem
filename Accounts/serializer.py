from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(
        write_only = True,
        required = True,
        style= {'input_type':'password'}
    )
    
    class Meta:
        model = User
        fields = ('username','email','password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self,attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self,**kwargs):
        # once we have token, we need refreshtoken to blacklist the token
        try:
            # request our token
            RefreshToken(self.token)
        except TokenError:
            # if we cant save it in blacklis
            self.fail('bad_token')