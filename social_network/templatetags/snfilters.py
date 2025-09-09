from django import template
from django.contrib.auth import get_user_model
from django.db.models import Q

from social_network.models import Friendship, Subscribe, Post, Like, Diss_like, Comment, Like_comment

User = get_user_model()

register = template.Library()

@register.filter
def friends_check(owner:User, user:User):
    return Friendship.objects.filter(Q(user = user, friend = owner) | Q(friend = user, user = owner)).exists()

@register.filter
def follow_check(owner:User, user:User):
    return Subscribe.objects.filter(Q(user = user, follower = owner) | Q(follower = user, user = owner)).exists()

@register.filter
def like_check(post:Post, user:User):
    return Like.objects.filter(post=post, post_follower=user).exists()

@register.filter
def comment_like_check(comment:Comment, user:User):
    return Like_comment.objects.filter(comment=comment, comment_follower=user).exists()

@register.filter
def disslike_check(post:Post, user:User):
    return Diss_like.objects.filter(post=post, post_follower=user).exists()