from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = [
        'Django', 
        'Python', 
        'git',
    ]

    list_posts = Post.objects.filter(deleted=False)

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologia':lista,
        'post':list_posts,}
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post':post})