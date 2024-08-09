from datetime import datetime as dt

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido!")

def alumno(request):
    texto = "Vista alumnos"
    return HttpResponse(texto)

def profesores(request):
    return HttpResponse("Vista profesores")

def cursos(request):
    return HttpResponse("Vista cursos")

def fecha_de_hoy(request):
    dia = dt.now()
    dia = dia.strftime("%Y-%m-%d")
    texto = f"La fecha de hoy es:<br>{dia}"
    return HttpResponse(texto)

def probando_template(request):
    
    nombre = "Adrian"
    apellido = "Holovaty"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    
    # Abrimos el archivo html
    mi_html = open('./Project_1/plantillas/index.html')
    
    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())
    
    # Creamos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()
    
    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para
    mi_contexto = Context(diccionario)
    
    # Terminamos de construir el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)