from cgitb import lookup
from unittest.util import three_way_cmp
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime 

from rest_framework import generics,permissions,status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from .serializer import ProfileSerializer,CategorySerializer,VehicleSerializer, RentVehicleSerializer
from .models import *
from .utils import Util
from decouple import config


# Create your views here.
class ViewProfile(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get(self,request):
        queryset = Profile.objects.get(user = self.request.user)
        serializer = ProfileSerializer(queryset)
        return Response({
            'status':status.HTTP_200_OK,
            'data':serializer.data
        })

class UpdateProfile(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProfileSerializer

    def patch(self,request):
        try:
            queryset = Profile.objects.get(user = request.user)
            serializer = self.serializer_class(queryset,data = request.data, partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({
                'status':status.HTTP_202_ACCEPTED,
                'data':serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND
            })

class CreateReadCategoryView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CategorySerializer

    def get(self,request):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response({
            'status':status.HTTP_200_OK,
            'data':serializer.data
        })

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            'data':serializer.data,
            'message':'Created successfully'
        })

class UpdateCategoryView(generics.RetrieveUpdateAPIView):
    permissions_classes = (permissions.IsAuthenticated,permissions.IsAdminUser, )
    serializer_class = CategorySerializer

    def put(self,request,pk):
        try:
            category = Category.objects.get(pk = pk)
            serializer = self.serializer_class(category,data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({
                'status':status.HTTP_202_ACCEPTED,
                'data':serializer.data,
                'message':'Hurray!!Update Successful.'
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'category with this id does not exist. '
            })

class AvailableVehicles(generics.GenericAPIView):
    serializer_class = VehicleSerializer

    def get(self,request,pk):
        try:
            category = Category.objects.get(pk = pk)
            queryset = category.vehicles.filter(booked = False)
            if queryset.exists():
                serializer = self.serializer_class(queryset,many = True)
                return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,
                    'rate':serializer.data['rate'],
                })
            else:
                return Response({
                    'status':status.HTTP_204_NO_CONTENT
                })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
            })

class CreateReadVehicleView(generics.GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = VehicleSerializer
    lookup_field = 'id'

    def get(self,request,id):
        try:
            queryset= Category.objects.get(id=id)
            vehicles = queryset.vehicles.all()
            serializer = self.serializer_class(vehicles, many = True)
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Category of this id doesnot exist'
            })

    def post(self,request,id):
        try:
            queryset = Category.objects.get(id = id)
            serializer = self.serializer_class(data= request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save(category = queryset)
            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Created Successfully'
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Category of this id does not exist.'
            })

class UpdatedDetailVehicleView(generics.RetrieveUpdateAPIView):
    permissions_classes = (permissions.IsAuthenticated, )
    serializer_class = VehicleSerializer

    def get(self,request,pk):
        try:
            vehicle = Vehicle.objects.get(pk = pk)
            serializer = self.serializer_class(vehicle)
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Vehicle with this id does not exist. '
            })

    def put(self,request,pk):
        try:
            vehicle = Vehicle.objects.get(pk = pk)
            serializer = self.serializer_class(vehicle,data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({
                'status':status.HTTP_202_ACCEPTED,
                'data':serializer.data,
                'message':'Hurray!!Update Successful.'
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Vehicle with this id does not exist. '
            })

class RentVehicleView(generics.GenericAPIView):
    
    permissions_classes = ('permissions.IsAuthenticated', )
    serializer_class = RentVehicleSerializer

    def post(self,request,pk):
        user = request.user
        vehicle = Vehicle.objects.get(pk = pk)
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user,vehicle=vehicle)
        vehicle.booked = True
        vehicle.vehicle_status = 'not-available'
        vehicle.save()
        email_body = "You have successfully rented vehicle."
        data = {
            'email_body':email_body,
            'to_email':[user.email, ],
            'from_email':config('EMAIL_HOST_USER'),
            'email_subject':'Rent vehicles'
        }
        Util.send_email(data)
        return Response({
            'status':status.HTTP_201_CREATED,
            'data':serializer.data,
            'message':'Rented successfully'
        })

class UpdateDetailRentedVehicle(generics.RetrieveUpdateAPIView):
    permissions_classes = ('permissions.IsAuthenticated', )
    serializer_class = RentVehicleSerializer

    def get(self,request,pk):
        try:
            rented_vehicle = RentVehicle.objects.get(pk = pk)
            serializer = self.serializer_class(rented_vehicle)
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'No vehicle is booked with this id'
            })
            
    def put(self,request,pk):
        try:
            rented_vehicle = RentVehicle.objects.get(pk = pk)
            serializer = self.serializer_class(rented_vehicle, data = request.data)
            serializer.is_valid(raise_exception =True)
            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Update Successful'
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'No vechile seems to rented with this id'
            })

class CancelBooking(generics.GenericAPIView):
    permissions_classes = (permissions.IsAuthenticated)
    serializer_class = RentVehicleSerializer

    def patch(self,request,pk):
        try:
            rented_vehicle = RentVehicle.objects.get(pk = pk)
            if rented_vehicle.rented_at.time().hour > 12:
                return Response({
                    'status':status.HTTP_403_FORBIDDEN,
                    'message':"Sorry!you cant cancel booking now."
                })
            else:
                serializer = self.serializer_class(rented_vehicle,data = request.data, partial = True)
                serializer.is_valid(raise_exception = True)
                rented_vehicle.vehicle.booked = False
                rented_vehicle.vehicle.vehicle_status = 'available'
                rented_vehicle.vehicle.save()
                serializer.save()
                return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,
                    'message':"Booking Cancel Successful",
                })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'You have not rented vehicle with this id'
            })
        
class ReturnVehicleView(generics.GenericAPIView):
    permissions_classes = (permissions.IsAuthenticated, )
    serializer_class = RentVehicleSerializer

    def post(self,request,pk):
        try:
            rented_vehicle = RentVehicle.objects.get(pk = pk)
            rented_vehicle.returned = True
            # serializer = self.serializer_class(rented_vehicle,data = request.data)
            # serializer.is_valid(raise_exception = True)
            rented_vehicle.vehicle.booked = False
            rented_vehicle.vehicle.vehicle_status = 'available'
            rented_vehicle.vehicle.save()
            rented_vehicle.save()
            # serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                # 'data':serializer.data,
                'message':"Thank you.Please Visit Again."
            })
        except ObjectDoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'No rented vehicles found.Please check id'
            })


            


































