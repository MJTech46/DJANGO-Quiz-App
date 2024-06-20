from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .utils import custom_upload

class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    icon = models.ImageField(upload_to=custom_upload, null=True, blank=True)
    lifeTime_coins = models.BigIntegerField(default=0, null=False)
    current_coins = models.BigIntegerField(default=0, null=False)
    
    def delete(self, *args, **kwargs):
        # Delete the associated file
        self.icon.delete()
        # Call the superclass delete method
        super().delete(*args, **kwargs)
