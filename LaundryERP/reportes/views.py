from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReporteForm
from .models import Reporte

# Create your views here.


def crear_reporte(request):
    reporte = Reporte.objects.all()
    return render(request, 'reportes/crear_reporte.html', {'reporte': reporte})
