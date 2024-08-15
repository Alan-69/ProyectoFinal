from django.shortcuts import render
from django.http import HttpResponse
from AppAlan.models import *
from AppAlan.forms import *
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor, Entregable
from django.urls import reverse_lazy

def inicio(request):
    return render(request, "AppAlan/index.html")

def cursos(request):
    return render(request, "AppAlan/cursos.html")

def profesores(request):
    return render(request, "AppAlan/profesores.html")

def estudiantes(request):
    return render(request, "AppAlan/estudiantes.html")
@login_required
def entregables(request):
    return render(request, "AppAlan/entregables.html")

def login(request):
    return render(request, "AppAlan/index.html")

def crear_cuenta(request):
    return render(request, "AppAlan/index.html")

def curso_formulario(request):
    #print(request.POST)
    #print("\n\n")
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso
        curso = Curso(
            nombre=request.POST['curso'],
            camada=request.POST['camada']
        )
        curso.save()
        
        return render(request, "AppAlan/cursos.html")
    return render(request,"AppAlan/curso_formulario.html")

def profesor_formulario(request):

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            profesor = Profesor
        profesor = Profesor(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido']
        )
        profesor.save()
        
        return render(request, "AppAlan/profesores.html")
    return render(request,"AppAlan/profesor_formulario.html")

def estudiante_formulario(request):
    #print(request.POST)
    #print("\n\n")
    if request.method == 'POST':
        mi_formulario = EstudianteFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            estudiante = Estudiante
        estudiante = Estudiante(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email']
        )
        estudiante.save()
        
        return render(request, "AppAlan/estudiantes.html")
    return render(request,"AppAlan/estudiante_formulario.html")

def entregable_formulario(request):
    if request.method == 'POST':
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            entregable = Entregable
        entregable = Entregable(
            nombre=request.POST['nombre'],
            fecha_de_entrega=request.POST['fecha_de_entrega'],
            entregado=request.POST['entregado']
        )
        entregable.save()
        
        return render(request, "AppAlan/entregables.html")
    return render(request,"AppAlan/entregable_formulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        #print (miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            
            return render(request,"AppAlan/index.html")
    else:
        mi_formulario = CursoFormulario()
        
    return render(request, "AppAlan/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre=informacion["curso"])
            
            return render(request, "AppAlan/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()
        
    return render(request, "AppAlan/buscar_form_con_api.html", {"mi_formulario": mi_formulario})

def inicio(request):
    formulario = FormularioBusquedaCurso()
    resultados = []

    if request.method == 'GET' and 'consulta' in request.GET:
        formulario = FormularioBusquedaCurso(request.GET)
        if formulario.is_valid():
            consulta = formulario.cleaned_data['consulta']
            resultados = Curso.objects.filter(nombre__icontains=consulta)  # Filtrar por el campo adecuado

    return render(request, 'AppAlan/index.html', {'formulario': formulario, 'resultados': resultados})

@login_required
def about(request):
    return render(request, "AppAlan/about.html")
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppAlan/curso_list.html"
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class CursoDetailView(DetailView):
    model = Curso
    
def cursos_todos(request):
    return render(request, "AppAlan/cursos_todos.html")