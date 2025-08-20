# In core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    
    # Add this line to include the cart URLs
    path('api/', include('orders.urls')), 
]