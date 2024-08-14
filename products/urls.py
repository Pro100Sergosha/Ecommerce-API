from django.urls import path, include
from .views import ProductViewset, ImageViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'images', ImageViewset)

urlpatterns = [
    path('', include(router.urls)),
]
