from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from .models import Post, Usuario

def my_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')
        if(User.objects.filter(username=usuario).exists()):
            user = authenticate(request,username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                messages.success(request, 'Bienvenido {}'.format(usuario))
                return redirect('/')
            else:
                messages.error(request, 'Contraseña incorrecta')
        else:
            messages.error(request, 'Usuario no existe')
    return render(request, 'login.html')

def my_logout(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('/')

def registro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')
        verif = request.POST.get('verif')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        if(contrasena != verif):
            messages.error(request, 'Contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username=usuario, password=contrasena, email=email, first_name=nombre)
        return redirect('/login')
    return render(request, 'registro.html')
def home(request):
    posts = Post.objects.all()
    #usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request,post_id=None):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        if(post_id is None):
            post = Post.objects.create(title=request.POST['titulo'], text=request.POST['texto'])
        else:
            post = Post.objects.get(id=post_id)
            post.title = request.POST['titulo']
            post.text = request.POST['texto']
            post.save()
    context = {}
    if post_id is not None:
        post = Post.objects.get(id=post_id)
        context['post'] = post
    return render(request, 'post.html', context)
    #return HttpResponse('<p>Esto es un ejemplo</p>')
