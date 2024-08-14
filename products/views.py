from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, ImageSerializer, ColorSerializer, BuyProductSerializer
from .models import Product, Image, Color


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    # def list(self, request, *args, **kwargs):
    #     products = Product.objects.filter()
    # @action(detail=False, methods=['post', 'get'], url_path='buy-product')
    # def buy_product(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         products = self.get_queryset()
    #         serializer = BuyProductSerializer(products, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     elif request.method == 'POST':
    #         serializer = BuyProductSerializer(data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         ...







class ColorViewset(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    # permission_classes = [IsAuthenticated]

class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [IsAuthenticated]
