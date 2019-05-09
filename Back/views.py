from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from .forms import AgregarUsuario, Login, Mascotas
from api.models import Usuario, Mascota
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
import json



#defino acciones posibles para establecer permisos
acciones=[
   {'Mostrar':'Home','url':'inicio'}
]
# Create your views here.

def index(request):
    return render(request, "index.html")

def salir(request):
    logout(request)
    return redirect('/')

#ingreso al sistema
def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('inicio')

    return render(request,"login.html",{'form':form,})

#vista para agregar usuarios nuevos y solo administrable por el staff
@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB,contacto=data.get("contacto"),region=data.get("region"),vivienda=data.get("vivienda"),perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})

#MASCOTAS

#vista para agregar mascotas nuevas y solo administrable por el staff
@login_required(login_url='login')
def gestionarMascota(request):
    actual=request.user
    form=Mascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        mascota=Mascota(codigoMascota=data.get("codigoMascota"),fotoMascota=data.get("fotoMascota"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascota=data.get("descripcionMascota"),estado=data.get("estado"))
        mascota.save()
    mascota=Mascota.objects.all()
    paginator = Paginator(mascota, 3)
    page = request.GET.get('page')
    mascota = paginator.get_page(page)
    form=Mascotas()
    return render(request,"GestionMascota.html",{'paginator':paginator,'actual':actual,'form':form,'mascota':mascota,'acciones':acciones,})



#lista de las mascotas solo de las disponibles
@login_required(login_url='login')
def lista(request):
    actual=request.user
    form=Mascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        mascota=Mascota(codigoMascota=data.get("codigoMascota"),fotoMascota=data.get("fotoMascota"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascota=data.get("descripcionMascota"),estado=data.get("estado"))
        mascota.save()
    mascota=Mascota.objects.filter(estado='Disponible')
    paginator = Paginator(mascota, 3)
    page = request.GET.get('page')
    mascota = paginator.get_page(page)
    form=AgregarUsuario()
    return render(request,"listaMascota.html",{'paginator':paginator,'actual':actual,'form':form,'mascota':mascota,'acciones':acciones,})

#permite al usuario llenar un formulario y registrarse en el sistema
def registro(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo"), data.get("password"))
        usuario=Usuario(user=regDB,contacto=data.get("contacto"),region=data.get("region"),vivienda=data.get("vivienda"),perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    contexto={
        'actual':actual, 
        'form':form, 
        'usuarios':usuarios,
        }
    return render(request, "registrarse.html", contexto)
