from django.shortcuts import render, redirect
import os
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile

from decimal import Decimal  # Asegúrate de importar Decimal
from django.contrib import messages  # Para usar mensajes flash
from django.core.exceptions import ObjectDoesNotExist

# Para el informe (Reporte) Excel
import pandas as pd

import json

import logging

from django.utils import timezone
from openpyxl import Workbook  # Para generar el informe en excel
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Usuario  # Importando el modelo de Usuario
from . models import Encuesta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Paguina de Login
def login(request):
    return redirect('login')

# Paguina de Inicio
def inicio(request):
    return render(request, 'index.html')


# Metodos para Graficas
def chart_data(request):
    data = (
        Encuesta.objects
        .values('favor_encuesta')
        .annotate(count=Count('favor_encuesta'))
    )
    return JsonResponse(list(data), safe=False)


from django.http import JsonResponse
from .models import Encuesta

def chart_data_razon_encuesta(request):
    # Obtener los datos de la base de datos
    encuestas = Encuesta.objects.all()
    razon_encuestas = set(encuesta.razon_encuesta for encuesta in encuestas)
    data = []

    # Iterar sobre cada razon_encuesta y contar su frecuencia
    for razon_encuesta in razon_encuestas:
        count = encuestas.filter(razon_encuesta=razon_encuesta).count()
        data.append({
            'razon_encuesta': razon_encuesta,
            'count': count
        })

    return JsonResponse(data, safe=False)

def chart_data_ventajas_encuesta(request):
    # Obtener los datos de la base de datos
    encuestas = Encuesta.objects.all()
    ventajas_encuestas = set(encuesta.ventajas_encuesta for encuesta in encuestas)
    data = []

    # Iterar sobre cada ventajas_encuesta y contar su frecuencia
    for ventajas_encuesta in ventajas_encuestas:
        count = encuestas.filter(ventajas_encuesta=ventajas_encuesta).count()
        data.append({
            'ventajas_encuesta': ventajas_encuesta,
            'count': count
        })

    return JsonResponse(data, safe=False)


def chart_data_desventajas_encuesta(request):
    # Obtener los datos de la base de datos
    encuestas = Encuesta.objects.all()
    desventajas_encuestas = set(encuesta.desventajas_encuesta for encuesta in encuestas)
    data = []

    # Iterar sobre cada desventaja_encuesta y contar su frecuencia
    for desventaja_encuesta in desventajas_encuestas:
        count = encuestas.filter(desventajas_encuesta=desventaja_encuesta).count()
        data.append({
            'desventajas_encuesta': desventaja_encuesta,
            'count': count
        })

    return JsonResponse(data, safe=False)

def chart_data_poraum_encuesta(request):
    # Obtener los datos de la base de datos
    encuestas = Encuesta.objects.all()
    poraum_encuestas = set(encuesta.poraum_encuesta for encuesta in encuestas)
    data = []

    # Iterar sobre cada poraum_encuesta y contar su frecuencia
    for poraum_encuesta in poraum_encuestas:
        count = encuestas.filter(poraum_encuesta=poraum_encuesta).count()
        data.append({
            'poraum_encuesta': poraum_encuesta,
            'count': count
        })

    return JsonResponse(data, safe=False)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'login.html')

# Listar Usuarios y Encuestas
def listar_usuarios(request):
    usuarios = Usuario.objects.all()  
    data = {
        'usuarios': usuarios,
    }
    return render(request, 'usuario/lista_usuarios.html', data)

def listar_encuestas(request):
    encuestas = Encuesta.objects.all()  
    data = {
        'encuestas': encuestas,
    }
    return render(request, 'encuesta/lista_encuesta.html', data)

# Detalles de Usuarios y Encuestas
def detalles_usuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        data = {"usuario": usuario}
        return render(request, "usuario/detalles.html", data)
    except Usuario.DoesNotExist:
        error_message = f"no existe ningún registro para la busqueda id: {id}"
        return render(request, "usuario/lista_usuarios.html", {"error_message": error_message})

def detalles_encuesta(request, id):
    try:
        encuesta = Encuesta.objects.get(id=id)
        data = {"encuesta": encuesta}
        return render(request, "encuesta/detalles_encuesta.html", data)
    except Encuesta.DoesNotExist:
        error_message = f"no existe ningún registro para la busqueda id: {id}"
        return render(request, "encuesta/lista_encuestas.html", {"error_message": error_message})

# Registro de Usuario y Encuesta
def registrar_usuario(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre_usuario')
        apellido = request.POST.get('apellido_usuario')
        email = request.POST.get('email_usuario')        
        password = request.POST.get('password_usuario')
        edad = request.POST.get('edad_usuario')
        telefono = request.POST.get('telefono_usuario')

        usuario = Usuario(
            nombre_usuario=nombre,
            apellido_usuario=apellido,
            email_usuario=email,
            password_usuario=password,
            edad_usuario=edad,            
            telefono_usuario=telefono,            
        )
        usuario.save()
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        messages.success(
            request, f"Felicitaciones, el Usuario {nombre} fue registrado correctamente 😉")
        return redirect('listar_usuarios')

    # Si no se ha enviado el formulario, simplemente renderiza la plantilla con el formulario vacío
    return render(request, 'usuario/form_usuario.html')

#Agregar Usuario en Inicio
def registrar_usuario_inicio(request):
    if request.method == 'POST':
        
        nombre = request.POST.get('nombre_usuario')
        apellido = request.POST.get('apellido_usuario')
        email = request.POST.get('email_usuario')        
        password = request.POST.get('password_usuario')
        edad = request.POST.get('edad_usuario')
        telefono = request.POST.get('telefono_usuario')

        usuario = Usuario(
            nombre_usuario=nombre,
            apellido_usuario=apellido,
            email_usuario=email,
            password_usuario=password,
            edad_usuario=edad,            
            telefono_usuario=telefono,            
        )
        usuario.save()
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        messages.success(
            request, f"Felicitaciones, el Usuario {nombre} fue registrado correctamente")
        return redirect('inicio')    
    return render(request, 'usuario/form_usuario_inicio.html')

def agregar_encuesta(request):
    if request.method == 'POST':
        salest = request.POST.get('salest_encuesta')
        favor = request.POST.get('favor_encuesta')
        poraum = request.POST.get('poraum_encuesta')        
        ultaum = request.POST.get('ultaum_encuesta')
        razon = request.POST.get('razon_encuesta')
        comact = request.POST.get('comact_encuesta')
        ventajas = request.POST.get('ventajas_encuesta')
        desventajas = request.POST.get('desventajas_encuesta')
    
        encuesta = Encuesta(
            salest_encuesta=salest,
            favor_encuesta=favor,
            poraum_encuesta=poraum,
            ultaum_encuesta=ultaum,
            razon_encuesta=razon,            
            comact_encuesta=comact,
            ventajas_encuesta=ventajas,
            desventajas_encuesta=desventajas,            
        )
        encuesta.save()

        messages.success(
            request, f"Felicitaciones, la {salest}Encuesta fue registrado correctamente 😉")
        return redirect('listar_encuestas')
    
    return render(request, 'encuesta/form_encuesta.html')


def view_form_update_usuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        opciones_edad = [(int(edad), int(edad)) for edad in range(18, 51)]

        data = {"usuario": usuario,
                'opciones_edad': opciones_edad,
                }
        return render(request, "usuario/form_update_usuario.html", data)
    except ObjectDoesNotExist:
        error_message = f"El Usuario con id: {id} no existe."
        return render(request, "usuario/lista_usuarios.html", {"error_message": error_message})

def view_form_update_encuesta(request, id):
    try:
        encuesta = Encuesta.objects.get(id=id)        

        data = {"encuesta": encuesta,                
                }
        return render(request, "encuesta/form_update_encuesta.html", data)
    except ObjectDoesNotExist:
        error_message = f"La Encuesta con id: {id} no existe."
        return render(request, "usuario/lista_usuarios.html", {"error_message": error_message})

# Actualizar usuario y encuesta
def actualizar_usuario(request, id):
    try:
        if request.method == "POST":            
            usuario = Usuario.objects.get(id=id)

            usuario.nombre_usuario = request.POST.get('nombre_usuario')
            usuario.apellido_usuario = request.POST.get('apellido_usuario')
            usuario.email_usuario = request.POST.get('email_usuario')
            usuario.password_usuario = request.POST.get('password_usuario')
            usuario.edad_usuario = int(request.POST.get('edad_usuario'))
            usuario.telefono_usuario = request.POST.get('telefono_usuario')

            usuario.save()
        return redirect('listar_usuarios')
    except ObjectDoesNotExist:
        error_message = f"El Usuario con id: {id} no se actualizó."
        return render(request, "usuario/lista_usuarios.html", {"error_message": error_message})

def actualizar_encuesta(request, id):
    try:
        if request.method == "POST":            
            encuesta = Encuesta.objects.get(id=id)

            encuesta.salest_encuesta = request.POST.get('salest_encuesta')
            encuesta.favor_encuesta = request.POST.get('favor_encuesta')
            encuesta.poraum_encuesta = request.POST.get('poraum_encuesta')        
            encuesta.ultaum_encuesta = request.POST.get('ultaum_encuesta')
            encuesta.razon_encuesta = request.POST.get('razon_encuesta')
            encuesta.comact_encuesta = request.POST.get('comact_encuesta')
            encuesta.ventajas_encuesta = request.POST.get('ventajas_encuesta')
            encuesta.desventajas_encuesta = request.POST.get('desventajas_encuesta')

            encuesta.save()
        return redirect('listar_encuestas')
    except ObjectDoesNotExist:
        error_message = f"La encuesta con id: {id} no se actualizó."
        return render(request, "usuario/lista_usuarios.html", {"error_message": error_message})
    

# Eliminar usuario y encuesta
def eliminar_usuario(request):
    if request.method == 'POST':
        id_usuario = json.loads(request.body)['idUsuario']
        # Busca el empleado por su ID
        usuario = get_object_or_404(Usuario, id=id_usuario)
        # Realiza la eliminación del empleado
        usuario.delete()
        return JsonResponse({'resultado': 1})
    return JsonResponse({'resultado': 1})

def eliminar_encuesta(request):
    if request.method == 'POST':
        id_encuesta = json.loads(request.body)['idEncuesta']
        # Busca el empleado por su ID
        encuesta = get_object_or_404(Encuesta, id=id_encuesta)
        # Realiza la eliminación del empleado
        encuesta.delete()
        return JsonResponse({'resultado': 1})
    return JsonResponse({'resultado': 1})

