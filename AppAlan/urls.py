from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from AppAlan import views

urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('ingresar/', views.login, name="Ingresar"),
    path('crear_cuenta/', views.crear_cuenta, name="Crear_Cuenta"),
    
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('profesor-formulario/', views.profesor_formulario, name="ProfesorFormulario"),
    path('estudiante-formulario/', views.estudiante_formulario, name="EstudianteFormulario"),
    path('entregable-formulario/', views.entregable_formulario, name="EntregableFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
    path('curso-list/', views.CursoListView.as_view, name="CursoListView"),
    path('about/', views.about, name="About"),
    path('cursos-todos/', views.cursos_todos, name="Cursos_Todos")
]

