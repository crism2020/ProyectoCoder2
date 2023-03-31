from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario, BusquedaCamada



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

def cursos(request):
    if request.method=="POST":
       miFormulario2=CursoFormulario(request.POST)
       print(miFormulario2)
       if miFormulario2.is_valid:
           informacion=miFormulario2.cleaned_data
           curso=Curso(nombre=informacion["curso"], camada=informacion["camada"])
           curso.save()
           return render(request, "AppCoder/inicio.html")
    else:
        miFormulario2=CursoFormulario() #formulario vacio para construir el html        
    return render(request, "AppCoder/cursos.html", {"miFormulario2":miFormulario2})

def profesorFormulario(request):
    if request.method=="POST":
       formulariop=ProfesorFormulario(request.POST)
       print(formulariop)
       if formulariop.is_valid:
           informacion=formulariop.cleaned_data
           profesor=Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
           profesor.save()
           return render(request, "AppCoder/inicio.html")
    else:
        formulariop=ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"formulariop":formulariop})

def busquedacamada(request):
    return render(request, "AppCoder/busquedacamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta=f"Estoy buscando la camada nro: {request.GET["camada"]}"
        camada=request.GET["camada"]
        cursos=Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/inicio.html", {"cursos": cursos, "camada":camada})
    else:
        respuesta="No enviaste datos"

    #return HttpResponse(respuesta)
    return render(request, "AppCoder/inicio.html", {"respuesta": respuesta})


