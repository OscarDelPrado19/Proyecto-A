from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm
#metodo que devuelve el json
def lista_productos(request):
    productos = Producto.objects.all()
    data = [
        {
            #Objeto construido al aire
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        } 
        for p in productos
    ]
    
    #Devolver la respuesta en formato json
    return JsonResponse(data, safe=False)

#Funcion para mandar a la vista del form
def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta del form
    if request.method == 'POST':
        #Si estamos recibiendo un form, entonces lo procesamos
        form = ProductoForm(request.POST)
        if form.is_valid():
            #Guardar el form en la base de datos
            form.save()
            #Redirigir a la lista de productos
            return redirect('agregar') #Redirigir a la lista de productos
    #pintar un form vacio
    else:
        #Si no estamos recibiendo un form, entonces lo mostramos
        form = ProductoForm()
  
    return render(request, 'agregar.html',{'form':form})