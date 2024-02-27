from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .models import *

# Create your views here.
@login_required(login_url='/auth/login/')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')


@login_required
def inscrever(request):
    if request.method == 'GET':
        return render(request, 'inscrever.html')
    
    
@login_required
def inscrever_fantasy(request):
    if request.method == 'GET':
        formulario = Fantasy_ModelForm()
        return render(request, 'inscrever_fantasy.html', {'formulario':formulario})
    
    elif request.method == 'POST':
        formulario = Fantasy_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            fantasy = formulario.save(commit=False)
            fantasy.usuario = request.user 
            fantasy.save()
            formulario = Fantasy_ModelForm()
            messages.add_message(request, constants.SUCCESS, 'Usuário inscrito com sucesso na categoria Fantasy!')
            return render(request, 'inscrever_fantasy.html', {'formulario':formulario})
        else:
            return render(request, 'inscrever_fantasy.html', {'formulario':formulario})
        
        
@login_required
def inscrever_makeyourself(request):
    if request.method == 'GET':
        formulario = Makeyourself_ModelForm()
        return render(request, 'inscrever_makeyourself.html', {'formulario':formulario})
    
    elif request.method == 'POST':
        formulario = Makeyourself_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            fantasy = formulario.save(commit=False)
            fantasy.usuario = request.user
            fantasy.save() 
            formulario = Makeyourself_ModelForm()
            messages.add_message(request, constants.SUCCESS, 'Usuário inscrito com sucesso na categoria Make Your Self!')
            return render(request, 'inscrever_makeyourself.html', {'formulario':formulario})
        else:
            return render(request, 'inscrever_makeyourself.html', {'formulario':formulario})
    
        
@login_required
def buscar_inscritos(request):
    form = FilterForm(request.GET)
    inscritos_fantasy = Fantasy.objects.all()
    inscritos_make = MakeYourSelf.objects.all()
    
    if request.method == 'GET':
        if form.is_valid():
            nome_completo_inicia_com = form.cleaned_data.get('nome_completo_inicia_com')
            if nome_completo_inicia_com:
                inscritos_fantasy = inscritos_fantasy.filter(nome_completo__startswith=nome_completo_inicia_com)
                inscritos_make = inscritos_make.filter(nome_completo__startswith=nome_completo_inicia_com)
    return render(request, 'inscritos.html', {'inscritos_fantasy':inscritos_fantasy, 'inscritos_make':inscritos_make, 'form':form})
    
      
@login_required
def apoiadores(request):
    if request.method == 'GET':
        return render(request, 'apoiadores.html')
    return render(request, 'apoiadores.html')


@login_required
def jurados(request):
    jurados = Jurado.objects.all()
    formulario = Jurado_ModelForm()
    
    if request.method == 'GET':
        return render(request, 'jurados.html', {'jurados':jurados, 'formulario':formulario})
    
    elif request.method == 'POST':
        formulario = Jurado_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            jurado = formulario.save(commit=False)
            jurado.usuario = request.user 
            jurado.save()
            formulario = Jurado_ModelForm()
            messages.add_message(request, constants.SUCCESS, 'Jurado cadastrado com sucesso!')
            return redirect('/home/jurados/')
        else:
            messages.add_message(request, constants.ERROR, 'Jurado não cadastrado!')
            return redirect('/home/jurados/')
    return redirect('/home/jurados/')
        
    
@login_required
def organizadores(request):
    organizadores = Organizadores.objects.all()
    formulario = Organizadores_ModelForm()
    if request.method == 'GET':
        return render(request, 'organizadores.html', {'organizadores':organizadores, 'formulario':formulario})
    
    elif request.method == 'POST':
        formulario = Organizadores_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            organizador = formulario.save(commit=False)
            organizador.save()
            formulario = Organizadores_ModelForm()
            messages.add_message(request, constants.SUCCESS, 'Organizador cadastrado com sucesso!')
            return redirect('/home/organizadores/')
        else:
            messages.add_message(request, constants.ERROR, 'Organizador não cadastrado!')
            return redirect('/home/organizadores/')
    return render(request, 'organizadores.html', {'organizadores':organizadores})


@login_required
def apoiadores(request):
    apoiadores = Apoiadores.objects.all()
    formulario = Apoiadores_ModelForm()
    if request.method == 'GET':
        return render(request, 'apoiadores.html', {'apoiadores':apoiadores, 'formulario':formulario})
    
    elif request.method == 'POST':
        formulario = Apoiadores_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            apoiador = formulario.save(commit=False)
            apoiador.save()
            formulario = Apoiadores_ModelForm()
            messages.add_message(request, constants.SUCCESS, 'Apoiador cadastrado com sucesso!')
            return redirect('/home/apoiadores/')
        else:
            messages.add_message(request, constants.ERROR, 'Apoiador não cadastrado!')
            return redirect('/home/apoiadores/')
    return render(request, 'apoiadores.html', {'apoiadores':apoiadores})

@login_required
def julgamento(request):
    if request.method == 'GET':
        return render(request, 'julgamento.html')
    return render(request, 'julgamento.html')



"""
TODO: criar um form para fantasy e um form para makeyourself, disponibilizar
cada um em sua respectiva view e jogar para o template dentro do modal.
depois avaliar com 2 jurados diferentes e ver o que acontece.
"""
@login_required
def julgamento_fantasy(request):
    form = FilterForm(request.GET)
    inscritos_fantasy = Fantasy.objects.all()
    
    if request.method == 'GET':
        if form.is_valid():
            nome_completo_inicia_com = form.cleaned_data.get('nome_completo_inicia_com')
            if nome_completo_inicia_com:
                inscritos_fantasy = inscritos_fantasy.filter(nome_completo__startswith=nome_completo_inicia_com)
    return render(request, 'julgamento_fantasy.html', {'inscritos_fantasy':inscritos_fantasy, 'form':form})
    


@login_required
def julgamento_makeyourself(request):
    if request.method == 'GET':
        return render(request, 'julgamento_makeyourself.html')
    return render(request, 'julgamento_makeyourself.html')