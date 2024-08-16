from django.contrib import admin
from .models import Product, Color, Image, MoreInfo, Video


admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(MoreInfo)
admin.site.register(Video)
