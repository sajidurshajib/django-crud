from rest_framework import serializers
from posts.models import Post, Catagory, Tag
from api.serializers import UserViewSerializer


class CatagorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    user = UserViewSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'user', 'created_at', 'updated_at')


class PostCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        p = Post.objects.create(**validated_data, user=user)
        return p
