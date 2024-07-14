from .models import Quiz, Option, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"

class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = "__all__"
