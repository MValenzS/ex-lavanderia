from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VentaForm
from .models import Venta

# Create your views here.


def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})


def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/detalle_venta.html', {'ventas': venta})


def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Venta ha sido creada con éxito!')
            return redirect('ventas:lista_venta')
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})


def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = Venta(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, f'La venta {
                             venta.id}  ha sido actualizada')
            return redirect('ventas:lista_ventas.html')
    else:
        # Pass the instance to the form for pre-filling the form fields with the current data.
        form = Venta(instance=venta)
    return render(request, 'venta/actualizar_venta.html', {'form': form, 'venta': venta})


def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, f'La venta {venta.id} ha sido eliminada')
        return redirect('ventas:lista_ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
