#Crear formularios para cada modulo de la App/modulo
from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nombre del producto',
                'required': True,
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio del producto',
                'required': True,
            }),
            'imagen': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL de la imagen',
                'required': True,
            }),
        }
        
        #Personalizar las etiquetas o textos que salen alado de los inputs
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen',
        }
        
        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre del producto es obligatorio',
            },
            'precio': {
                'required': 'El precio del producto es obligatorio',
            },
            'imagen': {
                'required': 'La URL de la imagen es obligatoria',
            },
        }