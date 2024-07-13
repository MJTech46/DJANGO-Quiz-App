from Account.models import CustomUser
from rest_framework import serializers

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
        ]
        read_only_fields = [
            "id",
            "username",
        ]
