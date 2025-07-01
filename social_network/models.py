from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Subscribe(models.Model):
    follower = models.ForeignKey(User, related_name="follows", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "user")


class Friendship(models.Model):
    friend = models.ForeignKey(User, related_name="my_friends", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="friends", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "friend")