# In products/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'total_stock', 'created']
    list_filter = ['created', 'updated', 'category']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description', 'price', 'image')
        }),
        ('Size Quantities', {
            'fields': (
                ('xs_quantity', 's_quantity'),
                ('m_quantity', 'l_quantity'),
                ('xl_quantity', 'xxl_quantity'),
                'xxxl_quantity'
            ),
            'description': 'Set the available quantity for each size'
        }),
    )
    
    def total_stock(self, obj):
        return obj.total_stock
    total_stock.short_description = 'Total Stock'
