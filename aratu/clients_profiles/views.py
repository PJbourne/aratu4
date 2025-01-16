from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def previsao(request):
    return render(request, 'previsao.html')

def mapadecalor(request):
    return render(request, 'mapadecalor.html')

def relatorio(request):
    return render(request, 'relatorio.html')

def data(request):
    return render(request, 'data.html')