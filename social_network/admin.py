from django.contrib import admin
from social_network.models import Subscribe, Friendship


# Register your models here.
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("follower", "user", "created_at")

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "created_at", "confirmed")