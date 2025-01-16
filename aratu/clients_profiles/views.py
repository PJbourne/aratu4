from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Bem-vindo à Home!</h1>")

def previsao(request):
    return render(request, 'templates/previsao.html')

def mapadecalor(request):
    return render(request, 'templates/mapadecalor.html')

def relatorio(request):
    return render(request, 'templates/relatorio.html')

def data(request):
    return render(request, 'templates/data.html')