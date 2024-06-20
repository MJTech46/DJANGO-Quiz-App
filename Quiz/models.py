from django.db import models
from uuid import uuid4
from django.conf import settings

User=settings.AUTH_USER_MODEL

class Quiz(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    
    DIFFICULTY_CHOICES = [
        (EASY, 'easy'),
        (MEDIUM, 'medium'),
        (HARD, 'hard'),
    ]

    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    question_text = models.TextField(unique=True, null=False)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default=EASY)
    participants = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.question_text



class Option(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="options") #related_name is the reverse relation
    option_text = models.TextField(null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.option_text
    