from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import *
from django.urls import path, include
urlpatterns = [

   
    path('', views.inicio, name='inicio'),  # Página donde se inicia todo
    path('agregar/', views.agregar_contacto_view, name='agregar_contacto'),  # Página para agregar contacto
    path('buscar/', views.buscar_contacto_view, name='buscar_contacto'),  # Página de búsqueda de contactos por nombre y listar porterior de resultados
    path('listar/', views.listar_contactos_view, name='listar_contactos'),  # Página para listar todos los contactos y posterior listar detalle del contacto
    path('borrar_contacto/<int:contacto_id>/', views.borrar_contacto, name='borrar_contacto'), # pagina para borrar un contacto
    path('agregar_telefono/<int:contacto_id>/', views.agregar_telefono_view, name='agregar_telefono'),  # Página para agregar teléfono
    path('ver_telefonos/<int:contacto_id>/', views.ver_telefonos_view, name='ver_telefonos'),  # Página para ver todos los teléfonos de un contacto
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('listar2/', views.listar_contactos_view2, name='listar_contactos2'),  # Página para listar todos los contactos y posteriormente borrar uno
    
    path('agenda/', views.agenda, name='agenda')

]