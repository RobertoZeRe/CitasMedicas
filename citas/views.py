from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .Forms import CitasForm
from .Forms import AreasForm
from .models import Citas
from .models import Especialidad
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'],   password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('citas') 
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Usuario ya existe'})

        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})

@login_required
def citas(request):

    citas = Citas.objects.filter(usuario=request.user, fecha_completada__isnull=True)
    return render(request, 'citas.html', {'citas': citas})

@login_required
def citas_completar(request):

    citas = Citas.objects.filter(usuario=request.user, fecha_completada__isnull=False).order_by('-fecha_completada')
    
    return render(request, 'citas.html', {'citas': citas})



@login_required
def crear_cita(request):
    citas = Citas.objects.filter(usuario=request.user, fecha_completada__isnull=True)
    especialidades = Especialidad.objects.all()
    if request.method == 'GET':
        return render(request, 'crear_cita.html',{'form': CitasForm, 'citas': citas, 'especialidades': especialidades})
    else:
    
        try:
            form = CitasForm(request.POST)
            nueva_cita= form.save(commit=False)
            nueva_cita.usuario = request.user
            nueva_cita.especialidad = request.POST['especialidad']
            nueva_cita.save()
            
            return redirect('citas')

        except ValueError:
            return render(request, 'crear_cita.html', {'form': CitasForm,'error': 'Porfavor Ingresa Datos validos'})

@login_required
def cita_detalle(request, cita_id):
    especialidades = Especialidad.objects.all()

    if request.method == 'GET':
        cita = get_object_or_404(Citas, pk=cita_id)
        form = CitasForm(instance=cita)
        return render(request, 'citas_detalle.html',{'cita': cita, 'form': form, 'especialidades': especialidades})    
    else:
        try:
            cita = get_object_or_404(Citas, pk=cita_id)  
            form = CitasForm(request.POST, instance=cita)
            
            form.save()
            return redirect('home')    
        except ValueError:
    
            return render(request, 'citas_detalle.html',{'cita': cita, 'form': form, 'error': "Error actualizando cita"})    

@login_required
def cita_completar(request, cita_id):
    cita = get_object_or_404(Citas, pk=cita_id, usuario=request.user)
    
    if request.method == 'POST':
        cita.fecha_completada = timezone.now()
        cita.save()
        return redirect('home')

@login_required
def cita_borrar(request, cita_id):
    cita = get_object_or_404(Citas, pk=cita_id, usuario=request.user)
    
    if request.method == 'POST':
        cita.fecha_completada = timezone.now()
        cita.delete()
        return redirect('home')
        
         

@login_required   
def signout(request):
    logout(request)
    return redirect('home') 

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o Contraseña Incorrectos' })
            
        else:
            login(request,user)
            return redirect('citas')


@login_required 
def crear_area(request):
        
    if request.method == 'GET':
        return render(request, 'crear_area.html',{'form': AreasForm})

    else:
    
        try:
            form = AreasForm(request.POST)
            nueva_area= form.save(commit=False)
            nueva_area.Nombre_Especialidad = request.POST['Nombre_Especialidad']
            
            nueva_area.save()
            
            return redirect('crear_area')
        
        except ValueError:
            return render(request, 'crear_area.html', {'form': AreasForm,'error': 'Porfavor Ingresa Datos validos'})
    
    

    