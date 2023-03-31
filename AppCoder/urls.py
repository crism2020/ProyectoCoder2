from django.urls import path
from AppCoder import views

urlpatterns =[

    path ("", views.inicio, name="Inicio"),
    path ("cursos", views.cursos, name="Cursos"),
    path ("profesores", views.profesores, name="Profesores"),
    path ("estudiantes", views.estudiantes, name="Estudiantes"),
    path ("entregables", views.entregables, name="Entregables"),
    #path("cursoFormulario", views.cursoFormulario, name="CursoFormulario"),
    path("profesorFormulario", views.profesorFormulario, name="ProfesorFormulario"),
    path("busquedacamada", views.busquedacamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),



]