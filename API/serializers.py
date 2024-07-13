# serializer for API (only)
from rest_framework import serializers
from .models import NotePad

class NotePadeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = NotePad
        fields = "__all__"
