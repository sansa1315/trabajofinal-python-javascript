from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Producto
# from .models import Order

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CreateProductForm(ModelForm):
    class Meta:
        model = Producto
        widgets={
            'descripcion': forms.Textarea(attrs={
                'rows':5,
                'cols':30
            }),
            
        }        
        # fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen']
        fields = '__all__'

class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'