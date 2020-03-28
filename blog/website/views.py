from django.http import HttpResponse
from django.shortcuts import render

def hello_blog(request):
    lista = [
        'Django', 
        'Python', 
        'git',
    ]
    data = {'name': 'Curso de Django 3', 'lista_tecnologia':lista}
    return render(request, 'index.html', data)
