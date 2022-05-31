from cgitb import lookup
from unittest.util import three_way_cmp
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics,permissions,status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from .serializer import ProfileSerializer,CategorySerializer,VehicleSerializer
from .models import *

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

    def post(self,request,pk):
        try:
            queryset = Category.objects.get(pk=pk)
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
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
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





























