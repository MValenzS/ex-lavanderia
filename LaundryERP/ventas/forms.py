from django import forms
from .models import OrdenDeServicio
from usuarios.models import Usuario
from ventas.models import Venta
from django.contrib.auth.forms import AuthenticationForm

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['orden_servicio', 'monto_total', 'metodo_pago']
        widgets = {
            'orden_servicio': forms.Select(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Monto Total'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
        }
    
    
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['orden_servicio'].queryset = OrdenDeServicio.objects.filter(pago_realizado=False)
        self.fields['metodo_pago'].queryset = Venta.METODOS_DE_PAGO
        
        