from django.shortcuts import render
from .models import Participante
from .forms import Form_Julgamento

# Create your views here.

def candidatos(request):
    participantes = Participante.objects.all()
    return render(request, 'fantasy/index.html', {'participantes': participantes})

def julgamento(request):
    if request.method == 'GET':
        form = Form_Julgamento()
        return render(request, 'fantasy/julgamento.html',{'form': form})

    else:
        return render(request, 'fantasy/julgamento.html')