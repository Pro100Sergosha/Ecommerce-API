from django.contrib import admin
from .models import Product, Color, Image, MoreInfo, Video


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('stock',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(MoreInfo)
admin.site.register(Video)
