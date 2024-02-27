from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages
from .utils import Validar_Cadastro

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        dados = request.POST
        nome = Validar_Cadastro.validar_nome(request, request.POST.get('nome')) 
        sobrenome = Validar_Cadastro.validar_sobrenome(request, request.POST.get('sobrenome')) 
        username = Validar_Cadastro.validar_username(request, request.POST.get('username')) 
        email = Validar_Cadastro.validar_email(request, request.POST.get('email'))
        print(email)
        senha = Validar_Cadastro.validar_senha(request, request.POST.get('senha')) 
        confirmar_senha = Validar_Cadastro.validar_confirmar_senha(request, senha, request.POST.get('confirmar_senha'))
        
        if not (nome and sobrenome and username and email and senha and confirmar_senha):
            return render(request, 'cadastro.html', {'dados': dados})
    
        # verificar se já existe um usuário com esse nickname
        usuario = User.objects.filter(username=username)
        
        # tentar cadastrar o usuário
        if usuario.exists():
            messages.add_message(request, constants.SUCCESS, 'Já existe um usuário com esse username')
            return render(request, 'cadastro.html', {'dados': dados})
        else:
            try:
                usuario = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=nome,
                    last_name=sobrenome,
                    password=senha,
                )
                usuario.save()
                messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com Sucesso')
                return redirect('/auth/login')
            except:
                messages.add_message(request, constants.ERROR, 'Erro ao cadastrar usuário')
                dados = {}
                return render(request, 'cadastro.html', {'dados': dados})
        
    
def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    
    elif request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuario = auth.authenticate(username=username, password=password)
        
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('/home/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos')
            return redirect('/auth/login')
    else:
        return redirect('/auth/login')
        
    
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

