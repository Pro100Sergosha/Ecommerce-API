from django.contrib import admin
from .models import Product, Color, Image, MoreInfo

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(MoreInfo)

