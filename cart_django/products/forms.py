from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: 
        # co ke thua modelform
        model = Product
        fields = ['name',
                    'number',
                    'price',
                    'describe',
                    'producer',
                    'image']
        # fields = '__all__' 
    # ke thua form (tu dinh nghia)
    # field1 = Form.CharField(label='Your name', max_length=100)
