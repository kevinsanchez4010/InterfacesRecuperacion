from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def error_404(request):
    return render(request, '404.htm') 

def shop(request):
    return render(request, 'shop.html')


# Sistema de Autenticación
def login_view(request):
    """Vista de login de usuario"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')


def logout_view(request):
    """Vista de logout de usuario"""
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente')
    return redirect('index')


@login_required(login_url='login')
def dashboard_view(request):
    """Vista privada - Panel de usuario"""
    context = {
        'user': request.user,
    }
    return render(request, 'private/dashboard.html', context)