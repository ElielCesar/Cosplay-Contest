# Create your views here.
from django.shortcuts import render, redirect
from .models import Participante, Julgamento
from .forms import Form_Julgamento
from django.db.models import Sum

# Create your views here.

def candidatos(request):
    participantes = Participante.objects.all()
    return render(request, 'makeyourself/index.html', {'participantes': participantes})


def julgamento_get(request, id):
    if request.method == 'GET':
        participante = Participante.objects.get(id=id)
        form = Form_Julgamento(initial={'participante': id})
        return render(request, 'makeyourself/julgamento.html',{'form': form, 'participante': participante})


def julgamento_post(request):
    if request.method == 'POST':
        form = Form_Julgamento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('makeyourself:candidatos')
        

def relatorio(request):
    part_nota_final = Participante.objects.annotate(soma_notas=Sum('julgamento__nota_final')).order_by('-soma_notas')
    julgamento = Julgamento.objects.all()
    return render(request, 'makeyourself/relatorio.html', {'part_nota_final':part_nota_final, 'julgamento':julgamento})
