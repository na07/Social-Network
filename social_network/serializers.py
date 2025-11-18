from rest_framework import serializers
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'image', 'author']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source='Autor'
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'published', 'author_id']