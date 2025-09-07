import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('kit', 'Kit'),
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('footwear', 'Footwear'),
        ('accessory', 'Accessory'),
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

    def __str__(self):
        return self.name