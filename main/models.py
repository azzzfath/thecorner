import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('goalkeeper', 'Goalkeeper'), 
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.IntegerField()            
    description = models.TextField()        
    thumbnail = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')  
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    stock = models.PositiveIntegerField(default=0) 
    rating = models.FloatField(default=0.0)       

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  

    def __str__(self):
        return f"{self.name} - {self.category}"

    @property
    def reduce_stock(self, amount=1):
        if self.stock >= amount:
            self.stock -= amount
            self.save()
            return True
        return False
    