from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='custom_user')
    level = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return self.user.username if self.user else "Anonymous User"
