# In products/views.py

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# This view now lists ALL products, without filtering by availability
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all() # We removed the filter that caused the error
    serializer_class = ProductSerializer

# This view retrieves a SINGLE product by its ID, now with all its variants
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # The lookup field should be 'pk' to match the <uuid:pk> in your URL
    lookup_field = 'pk'
