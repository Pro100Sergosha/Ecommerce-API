from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import *





class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class TechnicalInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = TechnicalInfo
        fields = '__all__'


class SizeWeightInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = SizeWeightInfo
        fields = '__all__'

class ScreenInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ScreenInfo
        fields = '__all__'

class MemoryInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = MemoryInfo
        fields = '__all__'

class CameraInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = CameraInfo
        fields = '__all__'

class PortsInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PortsInfo
        fields = '__all__'

class BatteryInfoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = BatteryInfo
        fields = '__all__'
    
class MoreInfoSerializer(WritableNestedModelSerializer):
    technical_info = TechnicalInfoSerializer(required = False)
    size_weight = SizeWeightInfoSerializer(required = False)
    screen_info = ScreenInfoSerializer(required = False)
    memory_info = MemoryInfoSerializer(required = False)
    camera_info = CameraInfoSerializer(required = False)
    ports_info = PortsInfoSerializer(required = False)
    battery_info = BatteryInfoSerializer(required = False)
    class Meta:
        model = MoreInfo
        fields = '__all__'


class ProductSerializer(WritableNestedModelSerializer):
    buy_quantity = serializers.IntegerField(write_only = True, required = False)
    more_info = MoreInfoSerializer(read_only=True)
    color_options = ColorSerializer(read_only=True)
    additional_images = ImageSerializer(many = True)
    image = ImageSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    stock = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'more_info': {'required': False},
        }

class BuyProductSerializer(WritableNestedModelSerializer):
    buy_quantity = serializers.IntegerField(write_only = True, required = True)
    more_info = MoreInfoSerializer(read_only=True, required = False)
    color_options = ColorSerializer(read_only=True, required = False)
    additional_images = ImageSerializer(read_only=True,many = True, required = False)
    image = ImageSerializer(read_only=True, required = False)
    color = ColorSerializer(read_only=True, required = False)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['stock']