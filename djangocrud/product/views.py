from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from product.models import Product
from .serializers import ProductSerializers
from django.http import Http404
from rest_framework import mixins, generics
from .custom_pagination import CustomProductPagination
from django.db.models import Q


class ProductAPI(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = CustomProductPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductAPIDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Shortest generic view
class ProductGeneric(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


@api_view(['GET'])
def custom_msg(request):
    product = Product.objects.all()
    serialize = ProductSerializers(product, many=True)
    return Response(serialize.data)

    # class ProductAPI(APIView):
    #     def get(self, request, *args, **kwargs):
    #         products = Product.objects.all().order_by('-id')
    #         serializer = ProductSerializers(products, many=True)
    #         return Response(serializer.data)

    #     def get_object(self, request,  id, format=None):
    #         try:
    #             return Product.objects.get(id=id)
    #         except Product.DoesNotExist:
    #             raise Http404

    #     def post(self, request, format=None):
    #         product = ProductSerializers(data=request.data)
    #         if product.is_valid():
    #             product.save()
    #         return Response(product.data)

    #     def patch(self, request, id, format=None):
    #         # product = self.get_object(id=id)

    #         product = Product.objects.get(id=id)
    #         serializer = ProductSerializers(product, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(serializer.data)

    #     def delete(self, request, id, format=None):
    #         product = Product.objects.get(pk=id)
    #         product.delete()
    #         return Response({'msg': 'Dleted'})

    # @api_view(['GET'])
    # def getProduct(request):
    #     products = Product.objects.all().order_by('-id')
    #     serializer = ProductSerializers(products, many=True)
    #     return Response(serializer.data)

    # @api_view(['POST'])
    # def postProduct(request):
    #     product = ProductSerializers(data=request.data)
    #     if product.is_valid():
    #         product.save()
    #     return Response(product.data)

    # @api_view(['PATCH'])
    # def updateProduct(request, id):
    #     product = Product.objects.get(id=id)
    #     serializer = ProductSerializers(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)

    # @api_view(['DELETE'])
    # def removeProduct(request, id):
    #     product = Product.objects.get(id=id)
    #     product.delete()
    #     return Response({'msg': 'Dleted'})
