from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class UserV1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
