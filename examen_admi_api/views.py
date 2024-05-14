from django.shortcuts import render
from django.http import JsonResponse
from .models import Respuesta
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def guardar_respuesta(request):
    if request.method == 'POST':
        datos = request.POST.get('respuesta', None)
        if datos:
            respuesta = Respuesta(respuesta_texto=datos)
            respuesta.save()
            return JsonResponse({'mensaje': 'Respuesta guardada exitosamente'})
    return JsonResponse({'error': 'Se esperaba una solicitud POST'})
