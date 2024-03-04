from django import forms 
from django.contrib.auth.models import User
from .models import *

class Fantasy_ModelForm(forms.ModelForm):
    class Meta:
        model = Fantasy
        fields = ['nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal']
        widgets = {
            'nome_completo':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'personagem':forms.TextInput(attrs={'class':'form-control'}),
        }
        

class Makeyourself_ModelForm(forms.ModelForm):
    class Meta:
        model = MakeYourSelf
        fields = ['nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal']
        widgets = {
            'nome_completo':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
            'personagem':forms.TextInput(attrs={'class':'form-control'}),
        }


class Jurados_ModelForm(forms.ModelForm):
    class Meta:
        model = Jurado
        fields = ['nome_completo', 'email', 'telefone', 'foto']
        widgets = {
        'nome_completo':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'telefone':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Organizadores_ModelForm(forms.ModelForm):
    class Meta:
        model = Organizadores
        fields = ['nome_completo', 'email', 'telefone', 'foto']
        widgets = {
        'nome_completo':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'telefone':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Apoiadores_ModelForm(forms.ModelForm):
    class Meta:
        model = Apoiadores
        fields = ['nome_completo', 'email', 'telefone', 'foto']
        widgets = {
        'nome_completo':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'telefone':forms.TextInput(attrs={'class':'form-control'}),
        }       

# formulários de filtragem
class FilterForm(forms.Form):
        nome_completo_inicia_com = forms.CharField(
        required=False,
        label='Nome completo inicia com',
        widget=forms.TextInput(attrs={'class':'form-control w-100', 'placeholder':'Digite um nome para pesquisa...'}),
    )
    
class Julgamento_Fantasy_ModelForm(forms.ModelForm):
    class Meta:
        model = Julgamento
        fields = ['nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_sustentabilidade', 'observacao']
        widgets = {
            'nota_estetica':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_criatividade':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_performance':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_sustentabilidade':forms.NumberInput(attrs={'class':'form-control'}),
            'observacao':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Julgamento_Makeyourself_ModelForm(forms.ModelForm):
    class Meta:
        model = Julgamento_MakeYourSelf
        fields = ['nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_sustentabilidade', 'observacao']
        widgets = {
            'nota_estetica':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_criatividade':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_performance':forms.NumberInput(attrs={'class':'form-control'}),
            'nota_sustentabilidade':forms.NumberInput(attrs={'class':'form-control'}),
            'observacao':forms.TextInput(attrs={'class':'form-control'}),
        }