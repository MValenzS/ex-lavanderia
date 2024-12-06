# Generated by Django 5.1.3 on 2024-12-05 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de Debito o Credito'), ('cheque', 'Cheque')], max_length=20)),
                ('orden_servicio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordenes.ordendeservicio')),
            ],
        ),
    ]
