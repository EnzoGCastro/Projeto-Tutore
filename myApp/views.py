from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def menuIniciar(request):
    return render(request, 'menuiniciar.html', locals())

def forum(request):
    return render(request, 'forumConteudo.html',locals())

def encontrarTutor(request):
    return render(request, 'pesquisaencontrartutor.html', locals())

def perfilAluno(request):
    return render(request, 'perfilAluno.html', locals())

def perfilTutor(request):
    return render(request, 'perfil.html', locals())

def aulaDesc(request):
    return render(request, 'auladescricao.html', locals())

def pagamento(request):
    return render(request, 'pagamento.html', locals())