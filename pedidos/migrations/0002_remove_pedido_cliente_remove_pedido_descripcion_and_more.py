# Generated by Django 5.0.7 on 2024-07-14 18:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_envio',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_recogida',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_recogida',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pedido',
            name='medida_alto',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='medida_ancho',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='medida_largo',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_producto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
