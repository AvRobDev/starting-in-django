from django.http import HttpResponse
"""
-Esta es una manera de crear una vista de manera pocha:
def inicio(request):

    return HttpResponse("Hola, este es el inicio")

-Esta la estructura dentro de nuestro archivo urls.py:
path('inicio/', views.inicio, name="inicio"),

"""
def inicio(request):

    return HttpResponse("Hola, este es el inicio")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("No eres mayor de edad")