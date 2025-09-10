import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # wajib
    price = models.IntegerField()            # wajib
    description = models.TextField()         # wajib
    thumbnail = models.URLField(blank=True, null=True)  # wajib
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')  # wajib
    is_featured = models.BooleanField(default=False)  # wajib

    stock = models.PositiveIntegerField(default=0)  # tambahan
    rating = models.FloatField(default=0.0)        # tambahan

    def __str__(self):
        return f"{self.name} - {self.category}"


