import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('kit', 'Kit'),
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('footwear', 'Footwear'),
        ('accessory', 'Accessory'),
    ]

    CATEGORY_SIZES = [
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
    ]

    # Mandatory attributes
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField(default="No description for this product")
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    # Additional attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.IntegerField()
    size = models.CharField(max_length=20, choices=CATEGORY_SIZES)
    date_added = models.DateTimeField(auto_now_add=True)
    sold_count = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    def reduce_stock(self, quantity=1):
        if quantity <= 0:
            return False
        if quantity > self.stock:
            return False
        self.stock -= quantity
        self.save()
        return True
    
    def add_stock(self, quantity):
        if quantity <= 0:
            return False
        self.stock += quantity
        self.save()
        return True
    
    def increment_sold_count(self, quantity=1):
        self.sold_count += quantity
        self.save()

    @property
    def is_best_selling(self):
        return self.sold_count > 20