from .models import Quiz, Option
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"

class QuizSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        #The API responds with data in this same order
        fields = [
            'id',
            'uuid',
            'question_text',
            'options',
            'category',
            'difficulty',
        ]
