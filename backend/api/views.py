from django.contrib.auth import models
from django.http import request
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .permissions import IsOwner
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from .models import *
from rest_framework import generics

# User API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Profile API
class ProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        queryset = Profile.objects.filter(user=self.request.user)
        return queryset

# Packages API

class PackagesListAPIView(generics.ListCreateAPIView):
    serializer_class = PackagesSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        queryset = Packages.objects.all()
        return queryset
    

class PackagesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PackagesSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        queryset = Packages.objects.all()
        return queryset

# Bookings API

class BookingsListAPIView(generics.ListCreateAPIView):
    serializer_class = BookingsSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        queryset = Bookings.objects.all()
        return queryset

class BookingsDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingsSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        queryset = Bookings.objects.filter(user=self.request.user)
        return queryset

# csrf_exempt to allow other domains to access our api methods