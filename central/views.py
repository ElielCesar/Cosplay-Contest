from typing import Any
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from .forms import *
from .models import *
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect

# esse bloco vai ser utilizado para as CBVs
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


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


class InscreverView(LoginRequiredMixin, TemplateView):
    template_name = 'inscrever.html'


class JulgamentoView(LoginRequiredMixin, TemplateView):
    template_name = 'julgamento.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


""" Classes de CRUD para inscritos na categoria Fantasy """
class InscreverFantasyView(LoginRequiredMixin, CreateView):
    model = Fantasy
    form_class = Fantasy_ModelForm
    template_name = 'fantasy_form.html'
    success_url = '/home/inscritos_fantasy/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Inscrito com sucesso na categoria Fantasy!')
        return response


class InscritosFantasyView(LoginRequiredMixin, ListView):
    model = Fantasy
    template_name = 'inscritos_fantasy.html'
    context_object_name = 'inscritos_fantasy'
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        nome_completo_inicia_com = self.request.GET.get('nome_completo_inicia_com', '')
        
        if nome_completo_inicia_com:
            queryset = queryset.filter(nome_completo__startswith=nome_completo_inicia_com)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm(self.request.GET or None)
        return context


class DeletarFantasyView(LoginRequiredMixin, DeleteView):
    model = Fantasy
    template_name = 'fantasy_confirm_delete.html'
    success_url = '/home/inscritos_fantasy/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inscrito'] = self.get_object()
        return context


""" Classes de CRUD para inscritos na categoria Make Your Self """
class InscreverMakeYourSelfView(LoginRequiredMixin, CreateView):
    model = MakeYourSelf
    form_class = Makeyourself_ModelForm
    template_name = 'makeyourself_form.html'
    success_url = '/home/inscritos_makeyourself/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Inscrito com sucesso na categoria Make Your Self!')
        return response


class InscritosMakeYourSelfView(LoginRequiredMixin, ListView):
    model = MakeYourSelf
    template_name = 'inscritos_makeyourself.html'
    context_object_name = 'inscritos_makeyourself'
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        nome_completo_inicia_com = self.request.GET.get('nome_completo_inicia_com', '')
        
        if nome_completo_inicia_com:
            queryset = queryset.filter(nome_completo__startswith=nome_completo_inicia_com)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['form'] = FilterForm(self.request.GET or None)
        return context


class DeletarMakeYourSelfView(LoginRequiredMixin, DeleteView):
    model = MakeYourSelf
    template_name = 'makeyourself_confirm_delete.html'
    success_url = '/home/inscritos_makeyourself/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inscrito'] = self.get_object()
        return context


""" Classe de CRUD para Julgamento na categoria Fantasy"""
class JulgamentoFantasyView(LoginRequiredMixin,CreateView):
    model = Julgamento
    form_class = Julgamento_Fantasy_ModelForm
    template_name = 'avaliar_fantasy_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inscrito_id = self.kwargs.get('inscrito_id')
        context['inscrito'] = get_object_or_404(Fantasy, pk=inscrito_id)
        # verificar se esse jurado já avaliou o candidato
        avaliacao_existente = Julgamento.objects.filter(participante_fantasy=inscrito_id, jurado=self.request.user).first()
        if avaliacao_existente:
            context['form'] = self.form_class(instance=avaliacao_existente)
        return context
    
    def form_valid(self, form):
        inscrito_id = self.kwargs.get('inscrito_id')
        
        avaliacao_existente = Julgamento.objects.filter(
            participante_fantasy_id=inscrito_id,
            jurado=self.request.user).first()
        
        if avaliacao_existente:
            form = self.form_class(self.request.POST, instance=avaliacao_existente)
        
        else:
            form.instance.jurado = self.request.user
            form.instance.participante_fantasy = get_object_or_404(Fantasy, pk=inscrito_id)
            
        form.save()
        messages.success(self.request, 'Sua avaliacão foi salva com sucesso!')
        return redirect('/home/inscritos_fantasy/')

 
