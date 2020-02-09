from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128)
    imagen = models.CharField(max_length=128)
    fecha = models.DateField(default=datetime.now())

