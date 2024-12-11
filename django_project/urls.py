"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.menuIniciar, name="home"),
    path("forum/", views.forum, name="forum"),
    path("encontrartutor/", views.encontrarTutor, name="encontrar-tutor"),
    path("perfilaluno/",views.perfilAluno, name = "perfil-aluno"),
    path("perfiltutor/",views.perfilTutor, name = "perfil-tutor"),
    path("minhasturmas/",views.minhasTurmas, name = "minhas-turmas"),
    path("minhasaulas/",views.minhasAulas, name = "minhas-aulas"),
    path("minhaspostagens/",views.minhasPostagens, name = "minhas-postagens"),
    path("auladescexemplo/", views.aulaDesc, name = "aula descricao"),
    path("pagamento/", views.pagamento, name = "pagamento"),
    path("criaraula/", views.criacaoAula, name = "criar-aula"),
]
