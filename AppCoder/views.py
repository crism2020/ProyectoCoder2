from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso



def curso(self, nombre, camada):
    curso=Curso(nombre=nombre, camada=camada)
    curso.save()
    documentoDeTexto=f"---Curso: {curso.nombre}  Camada: {curso.camada} creado!"

    return HttpResponse(documentoDeTexto)


def inicio (request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

