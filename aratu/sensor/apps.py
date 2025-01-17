from django.apps import AppConfig


class SensorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensor'

from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_air_quality_data, name='import_air_quality_data'),
]