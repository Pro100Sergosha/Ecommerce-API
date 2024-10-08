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
    technical_info = TechnicalInfoSerializer()
    size_weight = SizeWeightInfoSerializer()
    screen_info = ScreenInfoSerializer()
    memory_info = MemoryInfoSerializer()
    camera_info = CameraInfoSerializer()
    ports_info = PortsInfoSerializer()
    battery_info = BatteryInfoSerializer()
    class Meta:
        model = MoreInfo
        fields = '__all__'


class ProductSerializer(WritableNestedModelSerializer):
    buy_quantity = serializers.IntegerField(write_only = True, required = False)
    more_info = MoreInfoSerializer()
    color_options = ColorSerializer(many = True)
    additional_images = ImageSerializer(many = True)
    image = ImageSerializer()
    color = ColorSerializer()
    stock = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = { 
            'more_info': {'required': False},
        }

class BuyProductSerializer(WritableNestedModelSerializer):
    buy_quantity = serializers.IntegerField(write_only = True, required = True)
    more_info = MoreInfoSerializer(required = False)
    color_options = ColorSerializer(required = False)
    additional_images = ImageSerializer(many = True, required = False)
    image = ImageSerializer(required = False)
    color = ColorSerializer(required = False)
    
    class Meta:
        model = Product
        fields = '__all__'