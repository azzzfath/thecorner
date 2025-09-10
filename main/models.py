from django.db import models

# Create your models here.
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
    name = models.CharField(max_length=255)  
    price = models.IntegerField()            
    description = models.TextField()        
    thumbnail = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')  
    is_featured = models.BooleanField(default=False)  

    stock = models.PositiveIntegerField(default=0) 
    rating = models.FloatField(default=0.0)       
  

    def __str__(self):
        return f"{self.name} - {self.category}"

    @property
    def is_best_seller(self):
        return self.rating >= 4.5 and self.stock > 0

    def reduce_stock(self, amount=1):
        if self.stock >= amount:
            self.stock -= amount
            self.save()
            return True
        return False