from django.apps import AppConfig


class ClientsProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients_profiles'
    def ready(self):
        import clients_profiles.signals

from django.urls import path
from . import views

urlpatterns = [
    path('heatmap/', views.generate_heatmap, name='generate_heatmap'),
]
