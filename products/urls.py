from django.urls import path, include
from .views import ProductViewset, ImageViewset, ColorViewset, VideoViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'images', ImageViewset)
router.register(r'colors', ColorViewset)
router.register(r'videos', VideoViewset)

urlpatterns = [
    path('', include(router.urls)),
]
