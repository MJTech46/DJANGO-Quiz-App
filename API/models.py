from django.db import models

# Create your models here.

class NotePad(models.Model):
    title = models.TextField(null=False)
    content = models.TextField(null=False)
