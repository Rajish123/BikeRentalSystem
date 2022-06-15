from django.forms import ValidationError
from rest_framework import serializers,status
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import Payment, Profile,Category,Vehicle,RentVehicle,Bill

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

class BillSerializer(serializers.ModelSerializer):
    # payment = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Bill
        fields = ['rented_vehicle','returned_at','total_bill','bill_status']

class PaymentSerializer(serializers.ModelSerializer):
    # payment = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Payment
        fields = '__all__'
