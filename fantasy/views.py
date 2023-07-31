from django.shortcuts import render
from .models import Participante
from .forms import Form_Julgamento

# Create your views here.

def candidatos(request):
    participantes = Participante.objects.all()
    return render(request, 'fantasy/index.html', {'participantes': participantes})

def julgamento(request, id):
    if request.method == 'GET':
        participante = Participante.objects.get(id=id)
        form = Form_Julgamento()
        return render(request, 'fantasy/julgamento.html',{'form': form, 'participante': participante})

    else:
        # falta terminar o post
        return render(request, 'fantasy/julgamento.html')