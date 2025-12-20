"""
URL configuration for Prueba3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from AppPrueba import views

urlpatterns = [

    # -------------------------
    # Sucursal
    # -------------------------
    path('', views.home, name='home'),
    path('sucursal', views.sucursal_listar, name='sucursal_listar'),
    path('sucursal/nueva/', views.sucursal_crear, name='sucursal_crear'),
    path('sucursal/editar/<int:pk>/', views.sucursal_editar, name='sucursal_editar'),
    path('sucursal/eliminar/<int:pk>/', views.sucursal_eliminar, name='sucursal_eliminar'),
    path('sucursal/matriculas/<int:sucursal_id>/', views.matriculas_por_sucursal, name='sucursal_matriculas'),
    # -------------------------
    # Curso
    # -------------------------
    path('curso/alumnos/<int:curso_id>', views.alumnos_por_curso, name='alumnos_curso'),
    path('curso/', views.curso_listar, name='curso_listar'),
    path('curso/nuevo/', views.curso_crear, name='curso_crear'),
    path('curso/editar/<int:pk>/', views.curso_editar, name='curso_editar'),
    path('curso/eliminar/<int:pk>/', views.curso_eliminar, name='curso_eliminar'),

    # -------------------------
    # Alumno
    # -------------------------
    path('alumno/', views.alumno_listar, name='alumno_listar'),
    path('alumno/nuevo/', views.alumno_crear, name='alumno_crear'),
    path('alumno/editar/<int:pk>/', views.alumno_editar, name='alumno_editar'),
    path('alumno/eliminar/<int:pk>/', views.alumno_eliminar, name='alumno_eliminar'),


    # -------------------------
    # Matrícula
    # -------------------------
    path('matricula/', views.matricula_listar, name='matricula_listar'),
    path('matricula/nueva/', views.matricula_crear, name='matricula_crear'),
    path('matricula/editar/<int:pk>/', views.matricula_editar, name='matricula_editar'),
    path('matricula/eliminar/<int:pk>/', views.matricula_eliminar, name='matricula_eliminar'),

]
