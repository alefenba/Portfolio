from django.shortcuts import render
from .models import  Categoria, Inicio, Perfil, Projeto, Sobre

def index(request):

    # Home
    inicio = Inicio.objects.latest('updated')

    # About
    sobre = Sobre.objects.latest('updated')
    perfis = Perfil.objects.filter(sobre=sobre)

    # Skills
    categorias = Categoria.objects.all()

    # Portfolio
    projetos = Projeto.objects.all()
    

    context = {
        'inicio': inicio,
        'sobre': sobre,
        'perfis': perfis,
        'categorias': categorias,
        'projetos': projetos
    }


    return render(request, 'index.html', context)
