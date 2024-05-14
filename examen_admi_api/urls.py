
from django.urls import path
from .views import guardar_respuesta

urlpatterns = [
    path('guardar-respuesta/', guardar_respuesta, name='guardar_respuesta'),
    # Otras URLs de tu aplicación...
]