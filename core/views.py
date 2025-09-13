from django.shortcuts import render
from .models import Filme

def listar_filmes(request):
    filmes = Filme.objects.all()
    
    return render(request,'filmes/lista.html',{"filmes":filmes})
