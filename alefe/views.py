from django.shortcuts import render
from .models import  Categoria, Certificado, Inicio, Perfil, Projeto, Sobre

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
    
    certificados = Certificado.objects.all()

    context = {
        'inicio': inicio,
        'sobre': sobre,
        'perfis': perfis,
        'categorias': categorias,
        'projetos': projetos,
        'certificados': certificados
    }


    return render(request, 'index.html', context)
