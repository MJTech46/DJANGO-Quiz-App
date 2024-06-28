from rest_framework import serializers
from .models import NotePad
from Account.models import CustomUser

class NotePadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotePad
        fields = [
            "id",
            "title",
            "content",
        ]

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username"
        ]
