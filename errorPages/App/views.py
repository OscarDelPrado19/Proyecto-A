from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from App.utils import google_search
from .models import ErrorLog

def index(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def error_404_view(request, exception):
    render(request, '404.html', status=404)
    
def error_500_view(request, exception):
    render(request, '500.html', status=500)
    
def error(request):
    return 7/0

def onepage(request):
    return render(request,'onepage.html',status=200)

def prueba(request):
    #Como obtener información de un html?
    nombre = request.GET.get('nombre','')
    edad = request.GET.get('edad','')
    
    persona = {
        'nombres':nombre,
        'edad':edad,
        'descripcion': nombre + ' - ' + edad
    }
    
    persona2 = {
        'nombres':'Naomy',
        'edad':20,
        'descripcion':nombre + ' - ' + edad
    }
    persona3 = {
        'nombres':'Yessy',
        'edad':40,
        'descripcion':nombre + ' - ' + edad
    }
    
    if(persona['nombres'] == 'Oscar'):
        persona['descripcion'] = 'Bienvenido usuario administrador'
    
    print(persona['nombres'])
    conjunto = [persona, persona2,persona3]
    return render(
        request,
        'prueba.html',
        {
            'objeto':persona, 'saludo':'Hola Mundo', 'personas':conjunto
        }
    )
    
def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})