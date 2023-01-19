from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post, Usuario

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def ejemplo(request):
    return HttpResponse('<p>Esto es un ejemplo</p>')
