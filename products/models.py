# In products/models.py

from django.db import models
import uuid

# --- This model stays the same ---
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# --- SIMPLIFIED Product model with size quantities ---
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)
    
    # Size quantities
    xs_quantity = models.PositiveIntegerField(default=0, verbose_name="XS Quantity")
    s_quantity = models.PositiveIntegerField(default=0, verbose_name="S Quantity")
    m_quantity = models.PositiveIntegerField(default=0, verbose_name="M Quantity")
    l_quantity = models.PositiveIntegerField(default=0, verbose_name="L Quantity")
    xl_quantity = models.PositiveIntegerField(default=0, verbose_name="XL Quantity")
    xxl_quantity = models.PositiveIntegerField(default=0, verbose_name="XXL Quantity")
    xxxl_quantity = models.PositiveIntegerField(default=0, verbose_name="XXXL Quantity")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'name']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
    
    @property
    def available_sizes(self):
        """Returns a dictionary of available sizes and their quantities"""
        sizes = {
            'XS': self.xs_quantity,
            'S': self.s_quantity,
            'M': self.m_quantity,
            'L': self.l_quantity,
            'XL': self.xl_quantity,
            'XXL': self.xxl_quantity,
            'XXXL': self.xxxl_quantity,
        }
        return {size: qty for size, qty in sizes.items() if qty > 0}
    
    @property
    def total_stock(self):
        """Returns total stock across all sizes"""
        return (self.xs_quantity + self.s_quantity + self.m_quantity + 
                self.l_quantity + self.xl_quantity + self.xxl_quantity + 
                self.xxxl_quantity)
