from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm, EmpleadoRegistrerForm
from django.contrib.auth.decorators import login_required, user_passes_test  # Required for admin-only views.
from django.contrib import messages  # Required for flash messages.
from .models import Usuario 


app_name = 'usuarios'
def login_empleado(request):
    form=LoginForm(data=request.POST or None)
    
    if form.is_valid():
        usuario=authenticate(username=form.cleaned_data['username'], password=['password'])
        
        if usuario:
            login(request, usuario)
            return redirect('index')
        
    return render(request, 'usuarios/login.html', {'form':form})    

def logout_empleado(request):
    logout(request)
    return redirect('index')    
        
def is_admin(usuario):
    return usuario.rol =='admin'

@login_required
@user_passes_test(is_admin)
def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoRegistrerForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.set_password(form.cleaned_data['password'])
            empleado.save()
            messages.success(request,'Empleado registrado exitosamente.')
            return redirect('usuarios:lista_empleados')
    else:
        form = EmpleadoRegistrerForm()
    return render(request, 'usuarios/registrar_empleado.html', {'form': form})
            
@login_required
@user_passes_test(is_admin)
def lista_empleados(request):
    empleados = object = Usuario.objects.filter(rol='empleado')
    
    return render(request, 'usuarios/lista_empleados.html', {'empleados': empleados})

@login_required
@user_passes_test(is_admin)
def index_view(request):
    return render(request, 'usuarios/index.html')