# agenda/forms.py

from django import forms
from .models import Contacto, Telefono

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['tipo_telefono', 'direccion', 'telefono']
