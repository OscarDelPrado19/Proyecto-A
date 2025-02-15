from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
            'placeholder': 'Ingrese su contraseña',
            'title': 'Debe contener al menos 8 caracteres y máximo 20 caracteres, una mayúscula, un número y un caracter especial',
            'required': True,
            'minlength': 8,
            'maxlength': 20,
        }),
    )
        
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña',
            'required': True,
            'minlength': 8,
            'maxlength': 20,
        })
    )
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel']
        widgets = {
             'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo institucional',
                'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debe ser un correo institucional (@utez.edu.mx)',
                'maxlength': 100,
                'required': True,
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True,
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': True,
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu matricula',
                'pattern': '^\d{5}[A-Za-z]{2}\d{3}$',
                'title': 'Matrículas que no sean de UTEZ no serán aceptadas',
                'required': True,
                'minlength': 10,
                'maxlength': 10,
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'required': True,
                'minlength': 15,
                'maxlength': 110,
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono (10 dígitos)',
                'pattern': '^\d{10}$',
                'title': 'Debe ser un número de teléfono válido (10 dígitos)',
                'required': True,
                'minlength': 10,
                'maxlength': 10,
            }),

        }

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     pattern = r"^[a-zA-Z0-9]+@utez\.edu\.mx$"
    #     if not re.match(pattern, email):
    #         raise forms.ValidationError("El correo debe pertenecer al dominio @utez.edu.mx.")
    #     return email

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     if len(password) < 8:
    #         raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
    #     if not re.search(r"[!#$%&?]", password):
    #         raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, & o ?).")
    #     if not re.search(r"\d", password):
    #         raise forms.ValidationError("La contraseña debe contener al menos un número.")
    #     return password

    # def clean_control_number(self):
    #     control_number = self.cleaned_data.get("control_number")
    #     if not re.match(r"^\d{5}[A-Za-z]{2}\d{3}$", control_number):
    #         raise forms.ValidationError("La matrícula debe tener el formato correcto.")
    #     return control_number
    
    # def clean_tel(self):
    #     tel = self.cleaned_data.get("tel")
    #     if not re.match(r"^\d{10}$", tel):
    #         raise forms.ValidationError("El número de teléfono debe tener 10 dígitos.")
    #     return tel

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data
        
    # if password1 and password2:
    #     if password1 != password2:
    #         raise forms.ValidationError("Las contraseñas no coinciden.")

    
    


class CustomUserLoginForm(AuthenticationForm):
    pass
