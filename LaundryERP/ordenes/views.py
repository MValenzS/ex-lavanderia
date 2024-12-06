from django.shortcuts import render, redirect, get_object_or_404
from .models import OrdenDeServicio
from .forms import OrdenDeServicioForm
from django.contrib import messages

# Create your views here.


def lista_ordenes(request):
    ordenes = OrdenDeServicio.objects.all()
    return render(request, 'ordenes/lista_ordenes.html', {'ordenes': ordenes})


def detalle_orden(request, id):
    orden = get_object_or_404(OrdenDeServicio, id=id)
    return render(request, 'ordenes/detalle_orden.html', {'orden': orden})


def crear_orden(request):
    if request.method == 'POST':
        form = OrdenDeServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Orden ha sido creada con éxito!')
            return redirect('ordenes/lista_ordenes')
    else:
        form = OrdenDeServicioForm()
    return render(request, 'ordenes/crear_orden.html', {'form': form})


def actualizar_estado(request, id):
    orden = get_object_or_404(OrdenDeServicio, id=id)
    if request.method == 'POST':
        estado = request.post.get('estado')
        orden.estado = estado
        orden.save()
        messages.success(request, f'La Orden {orden.id}  ha sido actualizado a {estado}')
        return redirect('ordenes:detalle_orden.html', id=orden.id)
        
    return render(request, 'ordenes/actualizar_estado.html', {'orden': orden})


def eliminar_orden(request, id):
    orden = get_object_or_404(OrdenDeServicio, id=id)
    if request.method == 'POST':
        orden.delete()
        messages.success(request, f'La Orden {orden.id} ha sido eliminada')
        return redirect('ordenes:lista_ordenes')
    return render(request, 'ordenes/eliminar_orden.html', {'orden': orden})
