import os
from django.http import JsonResponse
from django.core.management import call_command

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

def generate_heatmap(request):
    pm_type = request.GET.get('pm_type', 'pm10m')  # Padrão: pm10m
    try:
        call_command('generate_heatmap', pm_type)
        return JsonResponse({'status': 'success', 'message': f'Heatmap gerado com sucesso para {pm_type}!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})