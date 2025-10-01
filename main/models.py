from django.db import models
from django.core.validators import MinValueValidator
import uuid
from django.contrib.auth.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(default="")
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='-')
    is_featured = models.BooleanField(default=False)

    # tambahan
    purchase_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_best_seller(self):
        return self.purchase_count > 10
        
    def increment_sell(self):
        self.purchase_count += 1
        self.save()

# CHALLANGE
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):
    bio = models.TextField(default="")
    books = models.ManyToManyField(Book)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



