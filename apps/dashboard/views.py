from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from apps.account.models import CustomUser, Caso, Contrato
from .forms import CasoForm, ContratoForm
from django.contrib import messages


@login_required
def pagar_contrato(request, contrato_id):
    cliente = request.user  # Suponiendo que el usuario actual es el cliente
    contratos = Contrato.objects.filter(cliente=cliente)  # Filtra los contratos del cliente actual
    
    context = {
        'contratos': contratos,
    }
    
    return render(request, 'pagar-contrato.html', context)


@login_required
def account(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('account-admin')
    else:
        return redirect('account-customer')

@login_required
def account_admin(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Acceso denegado")

    usuarios = CustomUser.objects.filter(is_staff=False)
    causas = Caso.objects.all()
    contratos = Contrato.objects.all()

    context = {
        'usuarios': usuarios,
        'causas': causas,
        'contratos' : contratos
    }

    return render(request, 'account-admin.html', context)

@login_required
def account_customer(request):
    if request.user.is_superuser or request.user.is_staff:
        return HttpResponseForbidden("Acceso denegado")
    

    causas = Caso.objects.filter(cliente=request.user)
    contratos = Contrato.objects.filter(caso__cliente=request.user)
    context = {
        'causas' : causas,
        'contratos': contratos,
    }

    return render(request, 'account-customer.html', context)

@login_required  
def buscar(request,pk):
    if pk!='':
        clientes=CustomUser.objects.get(rut=pk)
        context={'usuarios':clientes}
        if clientes:
            return render(request, 'modify-customer.html', context)

        else:
            context={'mensaje','Error - Usuario no encontrado'}
            return render(request,'account-admin.html',context)

@login_required  


#===========================EDITAR CLIENTE===============================================
@login_required
def editar_usuario(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        
        try:
            usuario = CustomUser.objects.get(rut=rut)
            usuario.nombre = nombre
            usuario.email = email
            usuario.save()
            messages.success(request, "Usuario modificado correctamente.")
        except CustomUser.DoesNotExist:
            messages.error(request, "Error - Usuario no encontrado.")
        except Exception as e:
            messages.error(request, f"Error - No se pudo modificar el usuario: {str(e)}")
    else:
        messages.error(request, "Error - Método de solicitud no permitido. Por favor, usa el método POST.")

    return redirect('account-admin')


#===========================EDITAR CAUSAS ADMIN===============================================
def editar_causa(request, pk):
    causa = get_object_or_404(Caso, pk=pk)
    if request.method == 'POST':
        form = CasoForm(request.POST, instance=causa)
        if form.is_valid():
            form.save()
            return redirect('account-admin')
    else:
        form = CasoForm(instance=causa)
    return render(request, 'modify-caso.html', {'form': form})

#===========================EDITAR CONTRATO ADMIN===============================================
def editar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('account-admin')
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'modify-contrato.html', {'form': form})

#===========================BORRAR CONTRATO===============================================

def eliminar_contrato(request,pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    contrato.delete()
    return redirect('account-admin') 

#===========================BORRAR CAUSAS===============================================

#aqui haras la funcion:

def eliminar_causa(request, pk):
    causa = get_object_or_404(Caso, pk=pk, cliente=request.user)
    if request.method == 'POST':
        causa.delete()
        return redirect('account-customer')  
    return redirect('account-customer')  

def eliminar_causa_admin(request,pk):
    causa = get_object_or_404(Caso, pk=pk)
    causa.delete()
    return redirect('account-admin') 


#===========================BORRAR CLIENTES===============================================
@login_required    
def delete(request,pk):
    context={}
    try:
        cliente=CustomUser.objects.get(rut=pk)
        cliente.delete()
        mensaje='Cliente Eliminado Exitosamente'
        clientes=CustomUser.objects.all()
        context={'usuarios':clientes,'mensaje':mensaje}
        return render(request,'account-admin.html',context)
    except:
        mensaje='Rut de Cliente no Existe'    
        clientes=CustomUser.objects.all()
        context={'usuarios':clientes,'mensaje':mensaje}
        return render(request,'account-admin.html',context) 
    

#===========================INSERTAR CASO===============================================
@login_required
def agregar_caso(request):
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            caso = form.save(commit=False)
            caso.abogado = request.user  # Asignar el abogado actual como el abogado del caso
            caso.save()
            messages.success(request, "Caso agregado correctamente.")
            return redirect('account-admin')
        else:
            messages.error(request, "Error al agregar el caso. Por favor, corrige los errores en el formulario.")
    else:
        form = CasoForm()
    return render(request, 'agregar-caso.html', {'form': form})

def listar_casos(request):
    causas = Caso.objects.all()
    return render(request, 'listar_casos.html', {'causas': causas})

def crear_contrato(request, caso_id):
    caso = get_object_or_404(Caso, id=caso_id)
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.caso = caso
            contrato.cliente = caso.cliente
            contrato.abogado = caso.abogado
            contrato.save()
            return redirect('account-admin')
        else:
            print(form.errors)  # Para ver los errores de validación en la consola del servidor
    else:
        form = ContratoForm()
    return render(request, 'crear_contrato.html', {'form': form, 'caso': caso})



    

