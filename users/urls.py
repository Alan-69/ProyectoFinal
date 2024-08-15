from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    #path('logout/', LogoutView.as_view(template_name="AppAlan/index.html"), name="Logout"),
    path('logout/', views.logout_view, name='logout'),
    path('editar_usuario/', views.editar_usuario, name="EditarUsuario"),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name="CambiarPass"),
]