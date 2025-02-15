from django.urls import path
from .views import *

urlpatterns = [
    path('json/', lista_categorias,name='json'),
    path('registrar/', agregar_categoria,name='registrar'),
    path('api/get/',cards_categorias, name='categorias'),
]