from django.http import HttpResponse
from datetime import date, time, datetime
from django.template import Template, Context
from django.template import loader

def saludar(request):
    return HttpResponse('Hola mundo!')

def seguda_vista(request):
    return HttpResponse('<h1>Hola, este es un título</h1>')

def saludo_nombre(request, nombre):
    documento = f'<h1>Hola {nombre}</h1>'
    return HttpResponse(documento)

def calcular_nacimiento(request, edad):
    anio_actual=datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f'<h1>Vos naciste en el año {anio_nacimiento}</h1>')


# def probandoHtml(request):
   
#     diccionario = {'nombre':'Pablo', 'apellido':'DLV', 'edad':47, 'lista_de_notas': [1,4,5,3,5,8,7]}

#     archivo=open(r'C:\Users\Usuario\Desktop\python projects\sitio_python\codecomunicacion\plantillas\template.html')
#     contenido=archivo.read()
#     archivo.close()
#     template=Template(contenido)
#     contexto=Context(diccionario)
#     documento=template.render(contexto)
#     return HttpResponse(documento)

def probandoHtml(request):
   
   diccionario = {'nombre':'Pablo', 'apellido':'DLV', 'edad':47, 'lista_de_notas': [1,4,5,3,5,8,7]}
   template = loader.get_template("template.html")
   documento = template.render(diccionario)
   return HttpResponse(documento)
