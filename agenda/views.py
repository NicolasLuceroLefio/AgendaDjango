from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, TelefonoForm
from django.http import HttpResponse
from .models import Contacto, Telefono
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@login_required
def agregar_contacto_view(request):  # vista de agregar un contacto a la agenda
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        telefono_form = TelefonoForm(request.POST)
        if contacto_form.is_valid() and telefono_form.is_valid():
            # Procesa los datos del formulario
            contacto = contacto_form.save()
            telefono = telefono_form.save(commit=False)
            telefono.contacto = contacto
            telefono.save()
            # Redirige a la página de inicio
            return redirect('agenda')
    else:
        contacto_form = ContactoForm()
        telefono_form = TelefonoForm()

    return render(request, 'agregar_contacto.html', {      # Ruta por defecto es agenda/templates/agregar_contacto.html
        'contacto_form': contacto_form,
        'telefono_form': telefono_form
    })


def inicio(request):                               # Pagina de inicio del sistema
    return render(request, 'inicio.html')


@login_required
def buscar_contacto_view(request):     # vista de buscar contacto por nombre
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    contactos = Contacto.objects.filter(nombre__icontains=query)  # Buscar contactos que coincidan

    return render(request, 'buscar_contacto.html', {
        'contactos': contactos,
        'query': query
    })
@login_required
def listar_contactos_view(request):
    contactos = Contacto.objects.all()  # Obtener todos los contactos
    return render(request, 'listar_contactos.html', {  # (parte de ver telefonos  de contacto , en listar contactos)
        'contactos': contactos
    })

@login_required
def listar_contactos_view2(request):
    contactos = Contacto.objects.all()  # Obtener todos los contactos
    return render(request, 'listar_contactos2.html', {  # (parte de ver telefonos y después borrar contacto)
        'contactos': contactos
    })

@login_required
def borrar_contacto(request, contacto_id):               # vista de borrar contacto
    contacto = get_object_or_404(Contacto, id=contacto_id)
    
    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos2')
    
    return render(request, 'borrar_contacto.html', {'contacto': contacto})

@login_required
def agregar_telefono_view(request, contacto_id):              # vista de agregar telefono a un contacto
    contacto = get_object_or_404(Contacto, id=contacto_id)

    if request.method == 'POST':
        telefono_form = TelefonoForm(request.POST)
        if telefono_form.is_valid():
            telefono = telefono_form.save(commit=False)
            telefono.contacto = contacto
            telefono.save()
            return redirect('agenda')
    else:
        telefono_form = TelefonoForm()

    return render(request, 'agregar_telefono.html', {
        'telefono_form': telefono_form,
        'contacto': contacto
    })

@login_required
def ver_telefonos_view(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    telefonos = Telefono.objects.filter(contacto=contacto)  # Obtener todos los teléfonos del contacto deseado

    return render(request, 'ver_telefonos.html', {
        'contacto': contacto,
        'telefonos': telefonos
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')  # Redirige a la página de inicio o donde desees


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio o donde desees =================================================
    else:
        form = AuthenticationForm()
    return render(request, 'inicio.html', {'form': form})

def agenda(request):                               # Pagina de inicio del sistema
    return render(request, 'agenda.html')