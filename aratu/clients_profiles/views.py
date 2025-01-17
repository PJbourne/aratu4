from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.shortcuts import render

def home(request):
    return render(request, 'clients_profiles/home.html')

def previsao(request):
    return render(request, 'clients_profiles/previsao.html')

def mapadecalor(request):
    return render(request, 'clients_profiles/mapadecalor.html')

def relatorio(request):
    return render(request, 'clients_profiles/relatorio.html')

def data(request):
    return render(request, 'clients_profiles/data.html')