# In products/serializers.py

from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    available_sizes = serializers.ReadOnlyField()
    total_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'description',
            'price',
            'image',
            'xs_quantity',
            's_quantity',
            'm_quantity',
            'l_quantity',
            'xl_quantity',
            'xxl_quantity',
            'xxxl_quantity',
            'available_sizes',
            'total_stock',
        ]
