from django.contrib import admin
from .models import Contacto, Telefono

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('contacto', 'tipo_telefono', 'direccion', 'telefono')
    search_fields = ('telefono', 'direccion')

