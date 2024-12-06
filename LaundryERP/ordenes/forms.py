from django import forms
from .models import OrdenDeServicio, Prenda, Cliente
from usuarios.models import Usuario
from django.contrib.auth.forms import AuthenticationForm


class OrdenDeServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenDeServicio
        fields = ['descripcion', 'estado', 'cliente', 'empleado']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(
    ), empty_label='Seleccione un Cliente', widget=forms.Select(attrs={'class': 'form-control'}))
    empleado = forms.ModelChoiceField(queryset=Usuario.objects.filter(
        rol='empleado'), empty_label='Seleccione un Empleado', widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(choices=OrdenDeServicio.ESTADOS, initial='pendiente',
                               widget=forms.Select(attrs={'class': 'form-control'}))
    prendas = forms.ModelMultipleChoiceField(queryset=Prenda.objects.all(
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(OrdenDeServicioForm, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['empleado'].widget.attrs.update({'class': 'form-control'})
        self.fields['prendas'].widget.attrs.update({'class': 'form-control'})
