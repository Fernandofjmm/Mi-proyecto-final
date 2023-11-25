# myapp/urls.py
from django.urls import path
from .views import home, lista_articulos, detalle_articulo

urlpatterns = [
    path('', home, name='home'),
    path('articulos/', lista_articulos, name='lista_articulos'),
    path('articulos/<int:articulo_id>/', detalle_articulo, name='detalle_articulo'),
]
