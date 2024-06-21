from django.shortcuts import render
from rest_framework import generics
from .models import NotePad
from .serializers import NotePadSerializer

# Allow: GET, POST, HEAD, OPTIONS.
class NotePadListCreate(generics.ListCreateAPIView):
    queryset = NotePad.objects.all()
    serializer_class = NotePadSerializer

# Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
class NotePadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotePad.objects.all()
    serializer_class = NotePadSerializer
    lookup_field = "pk"
