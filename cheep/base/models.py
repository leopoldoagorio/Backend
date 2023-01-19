from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    def __str__(self):
        return self.apellido