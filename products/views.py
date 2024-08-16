from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        method='post',
        operation_description="Buy product (Data must be send in the list of dictionaries, or an error occurs)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Product ID'),
                'buy_quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quanitity of product you want to buy'),
            },
            required=['id', 'buy_quantity'],
        ),
        responses={
            status.HTTP_200_OK: BuyProductSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad Request',
            status.HTTP_404_NOT_FOUND: 'Not Found',
            status.HTTP_405_METHOD_NOT_ALLOWED: 'Method Not Allowed'
        }
    )
    @action(detail=False, methods=['post', 'get'], url_path='buy-product')
    def buy_product(self, request, *args, **kwargs):
        if request.method == 'GET':
            products = self.get_queryset()
            serializer = BuyProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
                missing_fields = []
                products = []
                data = [data for data in request.data]
                for id, product_data in enumerate(data):
                    try:
                        if 'id' not in product_data:
                            missing_fields.append('id')
                        if 'buy_quantity' not in product_data:
                            missing_fields.append('buy_quantity')
                        product_id = product_data['id']
                        buy_quantity = product_data['buy_quantity']
                        product = Product.objects.get(id=product_id)

                    except KeyError as e:
                        errors = {field: ["This field is required."] for field in missing_fields}
                        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

                    except Product.DoesNotExist:
                        return Response({'message': f'Product with id {product.get("id")} does not exist'}, status=status.HTTP_404_NOT_FOUND)
                    
                    if product.quantity - product_data['buy_quantity'] < 0:
                        return Response({'message': 'Not enough product'}, status=status.HTTP_400_BAD_REQUEST)
                    elif product.quantity - product_data['buy_quantity'] == 0:
                        product.quantity -= product_data['buy_quantity']
                        product.stock = 'out of stock'
                    else:
                        product.quantity -= product_data['buy_quantity']
                    product.save()
                    products.append(product)
                serializer = BuyProductSerializer(products, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





class VideoViewset(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ColorViewset(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticated]

class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
