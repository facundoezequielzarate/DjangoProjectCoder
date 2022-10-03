from django.http import HttpResponse

import random
import datetime


def saludo(request):
    return HttpResponse("Saludos desde el Views File")


def saludo_con_nombre(request, nombre, apellido):
    hoy = datetime.datetime.now()
    return HttpResponse(f"Buenas Noches: {nombre.title{}} {apellido.title{}} <br> Hoy es {hoy}")


def saludo_con_template(request):
    mi_archivo = open()
    template = Template(mi_archivo.read(C: \Users\User\Documents\DjangoProjectCoder\Project1\Project1\templates\templates.html))
    mi_archivo.close()

    context = Context()

    result = template.render(context)
    return HttpResponse(result)

