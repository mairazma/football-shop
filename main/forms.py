from django.forms import ModelForm
from django import forms
from main.models import Products

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]

    