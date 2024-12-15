from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import requests

def register(request):
    form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # Esta vista probablemente será manejada por el frontend o la API
    return redirect('index')

def registration_complete(request):
    return render(request, 'registration_complete.html')

# Nuevas funciones para manejar la lógica de registro y login
def handle_register(request):
    if request.method == 'POST':
        try:
            # Endpoint de tu backend API para registro
            response = requests.post('https://tu-backend-api.com/api/register/', json=request.POST)
            
            if response.status_code == 201:
                messages.success(request, '¡Registro exitoso!')
                return redirect('registration_complete')
            else:
                # Maneja errores de la API
                errors = response.json().get('errors', {})
                for field, error_list in errors.items():
                    for error in error_list:
                        messages.error(request, f"Error en {field}: {error}")
                return redirect('register')
        
        except requests.exceptions.RequestException as e:
            messages.error(request, 'Error de conexión. Intente nuevamente.')
            return redirect('register')

def handle_login(request):
    if request.method == 'POST':
        try:
            # Endpoint de tu backend API para login
            response = requests.post('https://tu-backend-api.com/api/login/', json=request.POST)
            
            if response.status_code == 200:
                # Manejar token de autenticación
                token = response.json().get('token')
                # Guardar token en sesión o cookies
                request.session['auth_token'] = token
                return redirect('index')
            else:
                # Maneja errores de la API
                errors = response.json().get('errors', {})
                for error in errors:
                    messages.error(request, error)
                return redirect('login')
        
        except requests.exceptions.RequestException as e:
            messages.error(request, 'Error de conexión. Intente nuevamente.')
            return redirect('login')