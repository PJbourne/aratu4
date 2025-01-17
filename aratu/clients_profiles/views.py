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
    
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import folium
from folium.plugins import HeatMap
from sensor.models import AirQualityData


def generate_heatmap(request):
    pm_type = request.GET.get('pm_type', 'pm25m')  # Padrão é 'pm25m' caso não seja fornecido

    # Fetch data from the database
    data = AirQualityData.objects.values('lat', 'lon', pm_type)

    # Convert data to DataFrame
    df = pd.DataFrame.from_records(data)

    # Filter out rows where the PM value is NaN
    df = df.dropna(subset=[pm_type])

    # Drop rows with NaN in lat or lon
    df = df.dropna(subset=['lat', 'lon'])

    # Verifica se ainda há dados
    if df.empty:
        return JsonResponse({'error': 'No valid data to display. All selected PM values are NaN.'})

    # Seleciona as colunas de latitude e longitude
    locations = df[['lat', 'lon']].values.tolist()
    pm_values = df[pm_type].values.tolist()

    # Configuração do mapa
    center = [-20.27931919525688, -40.287294463682024]
    m = folium.Map(location=center, zoom_start=12)

    # Adiciona a camada de calor
    heat_data = [[loc[0], loc[1], pm] for loc, pm in zip(locations, pm_values)]
    HeatMap(heat_data, max_intensity=100, radius=8).add_to(m)

    # Retorna o mapa como HTML
    map_html = m._repr_html_()
    return JsonResponse({'map_html': map_html})
