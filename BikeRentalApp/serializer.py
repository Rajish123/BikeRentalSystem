from rest_framework import serializers,status
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import Profile,Category

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    
    class Meta:
        model = Profile
        fields = "__all__"


class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'