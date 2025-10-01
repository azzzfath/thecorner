from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'category', 'thumbnail', 'is_featured', 'brand']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'price': forms.NumberInput(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'input-field'}),
            'stock': forms.NumberInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'thumbnail': forms.URLInput(attrs={'class': 'input-field'}),
            'brand': forms.Select(attrs={'class': 'input-field'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'checkbox-field'}),
        }
