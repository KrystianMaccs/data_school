from rest_framework import serializers
from apps.blog.models import Post, PostTag, PostCategory


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

class PostTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostTag
        fields = "__all__"

class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = "__all__"