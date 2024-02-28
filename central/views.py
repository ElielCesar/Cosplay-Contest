from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants

# esse bloco vai ser utilizado para as CBVs
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


""" Classes de CRUD para Jurados"""
class JuradosCreateView(LoginRequiredMixin, CreateView):
    model = Jurado
    form_class = Jurados_ModelForm
    template_name = 'jurado_form.html'
    success_url = '/home/listar_jurados/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Jurado cadastrado com sucesso!')
        return response


class JuradosListView(LoginRequiredMixin, ListView):
    model = Jurado
    template_name = 'jurados.html'
    context_object_name = 'jurados'


class JuradosUpdateView(LoginRequiredMixin, UpdateView):
    model = Jurado
    form_class = Jurados_ModelForm
    template_name = 'jurado_form.html'
    success_url = '/home/listar_jurados/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Jurados atualizado com sucesso!')
        return response


class JuradosDeleteView(LoginRequiredMixin, DeleteView):
    model = Jurado
    template_name = 'jurado_confirm_delete.html'
    success_url = '/home/listar_jurados/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jurados'] = self.get_object()
        return context


""" Classes de CRUD para Organizadores"""
class OrganizadoresCreateView(LoginRequiredMixin, CreateView):
    model = Organizadores
    form_class = Organizadores_ModelForm
    template_name = 'organizador_form.html'
    success_url = '/home/listar_organizadores/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Organizador cadastrado com sucesso!')
        return response


class OrganizadoresListView(LoginRequiredMixin, ListView):
    model = Organizadores
    template_name = 'organizadores.html'
    context_object_name = 'organizadores'


class OrganizadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Organizadores
    form_class = Organizadores_ModelForm
    template_name = 'organizador_form.html'
    success_url = '/home/listar_organizadores/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Organizador atualizado com sucesso!')
        return response


class OrganizadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Organizadores
    template_name = 'organizador_confirm_delete.html'
    success_url = '/home/listar_organizadores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizador'] = self.get_object()
        return context


""" Classes de CRUD para Apoiadores"""
class ApoiadoresCreateView(LoginRequiredMixin, CreateView):
    model = Apoiadores
    form_class = Apoiadores_ModelForm
    template_name = 'apoiador_form.html'
    success_url = '/home/listar_apoiadores/'

    # em CBVs é assim que devem ser passadas as mensagens
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Apoiador cadastrado com sucesso!')
        return response


class ApoiadoresListView(LoginRequiredMixin, ListView):
    model = Apoiadores
    template_name = 'apoiadores.html'
    context_object_name = 'apoiadores'


class ApoiadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Apoiadores
    form_class = Apoiadores_ModelForm
    template_name = 'apoiador_form.html'
    success_url = '/home/listar_apoiadores/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Apoiador atualizado com sucesso!')
        return response


class ApoiadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Apoiadores
    template_name = 'apoiador_confirm_delete.html'
    success_url = '/home/listar_apoiadores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apoiador'] = self.get_object()
        return context


@login_required
def julgamento(request):
    if request.method == 'GET':
        return render(request, 'julgamento.html')
    return render(request, 'julgamento.html')


@login_required
def julgamento_fantasy(request):
    form = FilterForm(request.GET)
    inscritos_fantasy = Fantasy.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            nome_completo_inicia_com = form.cleaned_data.get(
                'nome_completo_inicia_com')
            if nome_completo_inicia_com:
                inscritos_fantasy = inscritos_fantasy.filter(
                    nome_completo__startswith=nome_completo_inicia_com)
    return render(request, 'julgamento_fantasy.html', {'inscritos_fantasy': inscritos_fantasy, 'form': form})


@login_required
def julgamento_makeyourself(request):
    if request.method == 'GET':
        return render(request, 'julgamento_makeyourself.html')
    return render(request, 'julgamento_makeyourself.html')


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
        return render(request, 'inscrever_fantasy.html', {'formulario': formulario})

    elif request.method == 'POST':
        formulario = Fantasy_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            fantasy = formulario.save(commit=False)
            fantasy.usuario = request.user
            fantasy.save()
            formulario = Fantasy_ModelForm()
            messages.add_message(
                request, constants.SUCCESS, 'Usuário inscrito com sucesso na categoria Fantasy!')
            return render(request, 'inscrever_fantasy.html', {'formulario': formulario})
        else:
            return render(request, 'inscrever_fantasy.html', {'formulario': formulario})


@login_required
def inscrever_makeyourself(request):
    if request.method == 'GET':
        formulario = Makeyourself_ModelForm()
        return render(request, 'inscrever_makeyourself.html', {'formulario': formulario})

    elif request.method == 'POST':
        formulario = Makeyourself_ModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            fantasy = formulario.save(commit=False)
            fantasy.usuario = request.user
            fantasy.save()
            formulario = Makeyourself_ModelForm()
            messages.add_message(
                request, constants.SUCCESS, 'Usuário inscrito com sucesso na categoria Make Your Self!')
            return render(request, 'inscrever_makeyourself.html', {'formulario': formulario})
        else:
            return render(request, 'inscrever_makeyourself.html', {'formulario': formulario})


@login_required
def buscar_inscritos(request):
    form = FilterForm(request.GET)
    inscritos_fantasy = Fantasy.objects.all()
    inscritos_make = MakeYourSelf.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            nome_completo_inicia_com = form.cleaned_data.get(
                'nome_completo_inicia_com')
            if nome_completo_inicia_com:
                inscritos_fantasy = inscritos_fantasy.filter(
                    nome_completo__startswith=nome_completo_inicia_com)
                inscritos_make = inscritos_make.filter(
                    nome_completo__startswith=nome_completo_inicia_com)
    return render(request, 'inscritos.html', {'inscritos_fantasy': inscritos_fantasy, 'inscritos_make': inscritos_make, 'form': form})
