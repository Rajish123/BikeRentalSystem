from rest_framework import serializers,status
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import Profile,Category,Vehicle,RentVehicle

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    
    class Meta:
        model = Profile
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    vehicles = serializers.StringRelatedField(many = True, read_only = True)
    
    class Meta:
        model = Category
        fields = ['type','image','vehicles']

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class RentVehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentVehicle
        fields = '__all__'


        