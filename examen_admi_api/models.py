from django.db import models

class Respuesta(models.Model):
    respuesta_texto = models.CharField(max_length=100) 