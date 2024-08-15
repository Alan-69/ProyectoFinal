from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()
    
    
class FormularioBusquedaCurso(forms.Form): 
    consulta = forms.CharField(label='Buscar cursos', max_length=100)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        help_text = {k: "" for k in fields}