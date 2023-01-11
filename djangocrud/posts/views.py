from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import APIView, action
from posts.models import Catagory, Tag, Post
from .serializers import CatagorySerializers, TagSerializers, PostSerializers, PostCreateSerializers


class CatagoryAPI(generics.ListCreateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializers


class CatagoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializers


class TagAPI(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class TagDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class PostAPI(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Post.objects.all()
    # serializer_class = PostSerializers
    serializer_map = {
        'GET': PostSerializers,
        'POST': PostCreateSerializers,
    }
