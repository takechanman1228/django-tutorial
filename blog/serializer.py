from rest_framework import serializers

from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')


class PostSerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ('id','title', 'text', 'created_date', 'published_date', 'author')
