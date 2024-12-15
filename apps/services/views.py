from django.shortcuts import render

def services(request):
    return render(request, 'services.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.account.models import Caso, CustomUser
from django.utils import timezone

@login_required
def solicitar_servicio(request):
    if request.method == 'POST':
        caso_nombre = request.POST.get('caso_nombre')
        cliente = request.user  # El cliente actualmente autenticado
        abogado = CustomUser.objects.filter(is_staff=True).first()  # Obtener un abogado (staff) cualquiera
        
        # Crear el caso en la base de datos
        caso = Caso.objects.create(
            nombre=caso_nombre,
            cliente=cliente,
            abogado=abogado,
            estado='Pendiente',  # Estado inicial del caso
            fecha_inicio=timezone.now(),  # Fecha de solicitud del servicio
            fecha_fin=None,  # Aún no hay fecha de fin definida
        )
        
        # Redireccionar a una página de confirmación o a donde sea necesario
        return redirect('services_complete')

    # Redirigir de vuelta a la página de servicios si no es POST
    return redirect('services')


def services_complete(request):
    return render(request, 'services-completed.html')

