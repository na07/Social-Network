from django import template
from django.contrib.auth import get_user_model
from django.db.models import Q

from social_network.models import Friendship, Subscribe

User = get_user_model()

register = template.Library()

@register.filter
def friends_check(owner:User, user:User):
    return Friendship.objects.filter(Q(user = user, friend = owner) | Q(friend = user, user = owner)).exists()

@register.filter
def follow_check(owner:User, user:User):
    return Subscribe.objects.filter(Q(user = user, follower = owner) | Q(follower = user, user = owner)).exists()