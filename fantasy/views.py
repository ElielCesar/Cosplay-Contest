from django.shortcuts import render
from .models import Participante

# Create your views here.

def candidatos(request):
    participantes = Participante.objects.all()
    return render(request, 'fantasy/index.html', {'participantes': participantes})