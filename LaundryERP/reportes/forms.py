from django import forms
from ordenes.models import OrdenDeServicio
from usuarios.models import Usuario
from reportes.models import Reporte
from django.contrib.auth.forms import AuthenticationForm

class ReporteForm(forms.ModelForm):
    class Meta:
        fields = ['id_orden_servicio', 'cliente', 'empleado','fecha_creacion','estado','total']
        
        widgets = {
            'id_orden_servicio': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Monto Total'}),

        }