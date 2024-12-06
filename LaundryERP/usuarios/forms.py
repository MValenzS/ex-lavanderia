from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
   pass

class EmpleadoRegistrerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'contraseña'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'confirmar contraseña'}))
    
    class Meta:
      model=Usuario
      fields=['username', 'first_name', 'last_name', 'email','rol']
        
      widgets={
         'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre de usuario'}),
         'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre '}),
         'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'apellido'}),
         'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'correo electronico'}),
         'rol': forms.Select(attrs={'class': 'form-control', 'placeholder':'selecciona un rol'}),
      }
      
      def clean(self):
         cleaned_data=super().clean()
         password=cleaned_data.get('password')
         confirm_password=cleaned_data.get('confirm_password')
         
         if password!=confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')
         return cleaned_data

     