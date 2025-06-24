from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    STATUS_CHOICES = (
        ("ONLINE", "Online"),
        ("OFFLINE", "Offline"),
        ("IDLE", "Idle"),
    )
    owner = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="OFFLINE")
    def __str__ (self):
        return f"Профиль {self.owner.username}"

