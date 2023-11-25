from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def lista_articulos(request):
    # Lógica para mostrar una lista de artículos
    return render(request, 'myapp/lista_articulos.html')

def detalle_articulo(request, articulo_id):
    # Lógica para mostrar detalles de un artículo
    return render(request, 'myapp/detalle_articulo.html', {'articulo_id': articulo_id})
