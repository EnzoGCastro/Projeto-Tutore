from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def minhasAulas(request):
    template = loader.get_template("../django_project/templates/minhasaulas.html")
    return HttpResponse(template.render())

def minhasPostagens(request):
    template = loader.get_template("../django_project/templates/minhaspostagens.html")
    return HttpResponse(template.render())

def minhasTurmas(request):
    template = loader.get_template("../django_project/templates/minhasturmas.html")
    return HttpResponse(template.render())

def minhas_aulas(request):
    template = loader.get_template("../django_project/templates/minhasaulas.html")
    return HttpResponse(template.render())
