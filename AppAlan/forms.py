from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class BuscaCursoForm(forms.Form):
    curso = forms.CharField()
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
class EntregableFormulario(forms.ModelForm):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()
    
    
class FormularioBusquedaCurso(forms.Form): 
    consulta = forms.CharField(label='Buscar cursos', max_length=100)
