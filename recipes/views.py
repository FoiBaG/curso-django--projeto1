from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fábio Goucha',
    })


def contato(request):
    return render(request, 'recipes/contatos.html')


def sobre(request):
    return HttpResponse('SOBRE')


# Create your views here.
