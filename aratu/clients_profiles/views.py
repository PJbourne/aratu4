from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Bem-vindo à Home!</h1>")
