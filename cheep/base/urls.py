from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post', views.post),
    path('post/<int:post_id>', views.post),
    path('login', views.my_login),
    path('logout', views.my_logout),
    path('registro', views.registro),
]