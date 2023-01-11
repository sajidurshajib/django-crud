from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, APIView
# from base.models import Items
from .serializers import RegisterSerializer, UserSerializer
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ===============================================


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        })

# ===============================================


class Logout(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


#  ===============================================


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def getData(request):
    return Response({'username': request.user.username})

    # q = request.GET.get('name') if request.GET.get('name') != None else ''
    # # pagination_class = CustomNamePagination
    # items = Items.objects.filter(Q(name__icontains=q)).order_by('-id')
    # serialize_items = ItemsSerializers(items, many=True)
    # return Response(serialize_items.data)


# @api_view(['POST'])
# def postData(request):
#     serializer = ItemsSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['PATCH'])
# def updateData(request, id):
#     item = Items.objects.get(id=id)
#     serializer = ItemsSerializers(item, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteData(request, id):
#     item = Items.objects.get(id=id)
#     item.delete()
#     return Response({'msg': 'Deleted'})
