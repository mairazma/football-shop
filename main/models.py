import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('training', 'Training'),
        ('merchandise', 'Merchandise'),
        ('protection', 'Protection')
    ]
    
    nama = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(default=0)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Sport')
    is_featured = models.BooleanField(default=False)

    # tambahan
    purchase_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    def is_best_seller(self):
        return self.purchase_count > 10
        
    def increment_sell(self):
        self.purchase_count += 1
        self.save()