from django.contrib import admin
from .models import Respuesta

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('respuesta_texto',)  # Especifica qué campos se mostrarán en la lista de respuestas
    search_fields = ('respuesta_texto',)  # Agrega campos de búsqueda

admin.site.register(Respuesta, RespuestaAdmin)
