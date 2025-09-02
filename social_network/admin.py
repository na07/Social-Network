from django.contrib import admin
from social_network.models import Subscribe, Friendship, Post, Category, Like, Diss_like, Comment


# Register your models here.
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("follower", "user", "created_at")

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "created_at", "confirmed")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'published', 'updated', 'status', 'category')
    search_fields = ('title', 'author__username', 'published')
    list_filter = ('status', 'category')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Like)
class Like(admin.ModelAdmin):
    pass

@admin.register(Diss_like)
class Diss_like(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass