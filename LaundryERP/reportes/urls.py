from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.crear_reporte, name='crear_reporte'),
  
]