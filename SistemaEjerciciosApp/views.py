from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("Home")

def ejercicios(request):

    return HttpResponse("Ejercicios")

def nosotros(request):

    return HttpResponse("Nosotros")

def blog(request):

    return HttpResponse("Blog")

def contacto(request):

    return HttpResponse("Contacto")
