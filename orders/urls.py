# In orders/urls.py

from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderViewSet # 1. Import OrderViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order') # 2. Register the new viewset

urlpatterns = router.urls