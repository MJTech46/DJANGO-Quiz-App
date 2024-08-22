from django.contrib import admin
from .models import Quiz, Option, Category, Reward

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Option)
admin.site.register(Category)
admin.site.register(Reward)
