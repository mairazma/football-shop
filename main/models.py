from django.db import models
import uuid

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('training', 'Training'),
        ('merchandise', 'Merchandise'),
        ('protection', 'Protection'),
        ('-', '-')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='-')
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