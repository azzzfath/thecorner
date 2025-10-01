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

    BRAND_CHOICES = [
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('puma', 'Puma'),
        ('under_armour', 'Under Armour'),
        ('reebok', 'Reebok'),
        ('mils', 'Mils'), 
        ('specs', 'Specs'),
        ('ortuseight', 'Ortuseight'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.IntegerField()            
    description = models.TextField()        
    thumbnail = models.URLField(blank=True, null=True, default='https://media.istockphoto.com/id/1147544809/vector/no-thumbnail-image-vector-graphic.jpg?s=170667a&w=0&k=20&c=v9QBkaN6fXxy1b-wsTQ6QhHUVGLo8JMMxhUBcWzOH0A=')  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')  
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0) 
    sold = models.PositiveIntegerField(default=0) 
    rating = models.FloatField(default=5.0)       
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  

    def __str__(self):
        return f"{self.name} - {self.category}"

    @property
    def reduce_stock(self, amount=1):
        if self.stock >= amount:
            self.stock -= amount
            self.sold += amount
            self.save()
            return True
        return False


    def get_brand_display(self):
        return self.brand.replace("_", " ").capitalize()
