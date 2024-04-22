#Se importa un atajo para renderizar nuestras plantillas(render)
from django.shortcuts import render

#Esta es la estructura basica de como llamar una plantilla dentro de nuestra carpeta templates, sin argumentos
def simple(request):

    return render(request, 'simple.html', {})