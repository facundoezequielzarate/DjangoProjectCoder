from django.http import HttpResponse

import random
import datetime

# Desde esta línea hasta la línea 63 quise utilizar esta idea para mostrar los familiares. Pienso que debe poder hacerse así pero le falta una vuelta de rosca
# Pero quise hacer algo distinto con cosas que ya hemos visto

class mi_familia:
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Madre(mi_familia):
    def saludo(self):
        print(f"Mi madre es: {self.nombre} {self.apellido} y tiene {self.edad} años")

mi_madre = Madre("Sarah", "Paulson", "47")
mi_madre.saludo()


class Padre(mi_familia):
    def saludo(self):
        print(f"Mi padre es: {self.nombre} {self.apellido} y tiene {self.edad} años")

mi_padre = Padre("Evan", "Peters", "35")
mi_padre.saludo()


class Hermano(mi_familia):
    def saludo(self):
        print(f"Mi hermano es: {self.nombre} {self.apellido} y tiene {self.edad} años")

mi_hermano = Hermano("Cody", "Fern", "30")
mi_hermano.saludo()


class Hermana(mi_familia):
    def saludo(self):
        print(f"Mi hermana es: {self.nombre} {self.apellido} y tiene {self.edad} años")

mi_hermana = Hermana("Elizabeth", "Olsen", "33")
mi_hermana.saludo()


def familiares(request):
    return HttpResponse(mi_madre.saludo(), mi_padre.saludo(), mi_hermano.saludo(), mi_hermana.saludo())


def texto(self):
    return HttpResponse("Esto es un texto")

def madree(self):
    return HttpResponse(mi_madre.saludo)

def padree(self):
    return HttpResponse(mi_padre.saludo)

def hermanoo(self):
    return HttpResponse(mi_hermano.saludo)

def hermanaa(self):
    return HttpResponse(mi_hermana.saludo)



def saludo_con_nombre_y_fecha(request, nombre):
    fecha = datetime.datetime.now()
    return HttpResponse(f"Saludos {nombre.title()}. Hoy es {fecha} <br> Que tengas buen día")


from django.template import Context, Template

def saludo_con_template(request):
    mi_archivo = open("/Users/User/Documents/DjangoProjectCoder/CoderProject/CoderProjec/t/CoderProject/templates/template.html")
    template = Template(mi_archivo.read())
    mi_archivo.close()

    context = Context()

    result = template.render(context)
    return HttpResponse(result)


def template_familiares(request):
    archivo = open("/Users/User/Documents/DjangoProjectCoder/CoderProject/CoderProject/CoderProject/templates/template-familiares.html")
    template = Template(archivo.read())
    archivo.close()

    context = Context()

    result = template.render(context)
    return HttpResponse(result)