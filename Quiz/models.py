from django.db import models
from uuid import uuid4
from django.conf import settings



class Category(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    category_text = models.TextField(unique=True, null=False)
    category_image = models.ImageField(upload_to="category/", default="default/category/default.png")

    def __str__(self) -> str:
        return self.category_text


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.question_text



class Option(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="options") #related_name is the reverse relation
    option_text = models.TextField(null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.option_text
    

class Reward(models.Model):
    reward_name = models.TextField(null=False)
    reward_value = models.IntegerField(null=False)
    reward_points_required = models.IntegerField(null=False)
    reward_image = models.ImageField(upload_to="reward/", default="default/reward/default.png")

    def __str__(self) -> str:
        return self.reward_name
