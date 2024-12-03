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

def aulasDescricao(request):
    template = loader.get_template("../django_project/templates/auladescricao.html")
    return HttpResponse(template.render())

def encontrarUmTutor(request):
    template = loader.get_template("../django_project/templates/encontrarumtutor.html")
    return HttpResponse(template.render())

def forumConteudo(request):
    template = loader.get_template("../django_project/templates/forumconteudo.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("../django_project/templates/logino.html")
    return HttpResponse(template.render())

def menuIniciar(request):
    template = loader.get_template("../django_project/templates/menuiniciar.html")
    return HttpResponse(template.render())

def pagamento(request):
    template = loader.get_template("../django_project/templates/pagamento.html")
    return HttpResponse(template.render())

def perfil(request):
    template = loader.get_template("../django_project/templates/perfil.html")
    return HttpResponse(template.render())

def perfilAluno(request):
    template = loader.get_template("../django_project/templates/perfilaluno.html")
    return HttpResponse(template.render())

def pesquisaEncontrarTutor(request):
    template = loader.get_template("../django_project/templates/pesquisaencontrartutor.html")
    return HttpResponse(template.render())

def telaMensagem(request):
    template = loader.get_template("../django_project/templates/telamensagem.html")
    return HttpResponse(template.render())