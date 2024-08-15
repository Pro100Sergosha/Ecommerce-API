from django.urls import path, include
from .views import ProductViewset, ImageViewset, ColorViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'images', ImageViewset)
router.register(r'colors', ColorViewset)

urlpatterns = [
    path('', include(router.urls)),
]
