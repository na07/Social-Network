from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



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

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        ('draft', "Draft"),
        ('published', "Published")
    )
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='posts')
    class Meta:
        ordering = ("-created", "-updated")

    def __str__(self):
        return self.title

class Like(models.Model):
    post_follower = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

class Diss_like(models.Model):
    post_follower = models.ForeignKey(User, related_name="disslikes", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="disslikes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post_follower", "post")


class Comment(models.Model):
    comment_maker = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

class Like_comment(models.Model):
    comment_follower = models.ForeignKey(User, related_name="comment_likes", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="comment_likes", on_delete=models.CASCADE)

