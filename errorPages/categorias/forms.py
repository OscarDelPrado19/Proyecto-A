from .models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Nombre de la categoria',
                'required': True,
            }),
            'imagen': forms.URLInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'URL de la imagen',
                'required': True,
            }),
        }
        
        #Personalizar las etiquetas o textos que salen alado de los inputs
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen',
        }
        
        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre de la categoria es obligatorio',
            },
            'imagen': {
                'required': 'La URL de la imagen es obligatoria',
            },
        }

