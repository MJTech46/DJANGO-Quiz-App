from django.shortcuts import render
from rest_framework import generics
from .models import NotePad
from Account.models import CustomUser
from .serializers import *

# Allow: GET, POST, HEAD, OPTIONS.
class NotePadListCreate(generics.ListCreateAPIView):
    queryset = NotePad.objects.all()
    serializer_class = NotePadSerializer

# Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
class NotePadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotePad.objects.all()
    serializer_class = NotePadSerializer
    lookup_field = "pk"

# Allow: GET, HEAD, OPTIONS
class UsernameRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsernameSerializer
    lookup_field = "username"