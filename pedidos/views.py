from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm

def index(request):
    ultimos_pedidos = Pedido.objects.order_by('-fecha_recogida')[:5]
    year = 2024
    context = {
        'ultimos_pedidos': ultimos_pedidos,
        'year': year,
    }
    return render(request, 'index.html', context)

def formulario_encomienda(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = PedidoForm()
    
    return render(request, 'formulario_encomienda.html', {'form': form})


def confirmacion(request):
    pedidos = Pedido.objects.all()
    context = {
        'mensaje': '¡Confirmación exitosa!'
    }
    return render(request, 'confirmacion.html', {'pedidos': pedidos})
