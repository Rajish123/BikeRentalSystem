from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics,permissions,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import ProfileSerializer
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