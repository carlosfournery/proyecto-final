"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, monstrar_familiares, mostrar_mascotas, mostrar_automoviles, 
                            BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BuscarMascota, AltaMascotas, ActualizarMascota, 
                            BuscarAutomovil, AltaAutomoviles, ActualizarAutomovil, FamiliarDetalle, FamiliarList,
                            FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from mi_blog.views import (index, PostDetalle, PostListar, PostCrear, 
                            PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('mi-familia/', monstrar_familiares),
    path('mascotas/', mostrar_mascotas),
    path('automoviles/', mostrar_automoviles),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mascotas/buscar', BuscarMascota.as_view()),
    path('automoviles/buscar', BuscarAutomovil.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mascotas/alta', AltaMascotas.as_view()),
    path('automoviles/alta', AltaAutomoviles.as_view()),
    # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('automoviles/actualizar/<int:pk>', ActualizarAutomovil.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('mi_blog/', index, name='mi_blog_index'),
    path('mi_blog/<int:pk>/detalle/', PostDetalle.as_view(), name="mi_blog_detalle"),
    path('mi_blog/listar/', PostListar.as_view(), name="mi_blog_listar"),
    path('mi_blog/crear/', PostCrear.as_view(), name="mi_blog_crear"),
    path('mi_blog/<int:pk>/borrar/', PostBorrar.as_view(), name="mi_blog_borrar"),
    path('mi_blog/<int:pk>/actualizar/', PostActualizar.as_view(), name="mi_blog_actualizar"),
    path('mi_blog/signup/', UserSignUp.as_view(), name="mi_blog_signup"),
    path('mi_blog/login/', UserLogin.as_view(), name="mi_blog_login"),
    path('mi_blog/logout/', UserLogout.as_view(), name="mi_blog_logout"),
]