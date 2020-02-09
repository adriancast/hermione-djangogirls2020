from django.shortcuts import render
from .models import Event

def items(request):
    eventos = Event.objects.all()
    return render(request, 'index.html', {'eventos': eventos})
