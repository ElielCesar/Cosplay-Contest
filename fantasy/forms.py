from django import forms
from .models import Participante, Jurado, Julgamento
from django.forms import Select


class Form_Julgamento(forms.ModelForm):
    class Meta:
        model = Julgamento
        fields = ['participante', 'jurado', 'nota_estetica', 'nota_criatividade', 'nota_performance', 'observacao']

        widgets = {
            'participante': Select(attrs={'class': 'form-control'}),
            'jurado': Select(attrs={'class': 'form-control'}),
            'nota_estetica': forms.TextInput(attrs={'class': 'form-control'}),
            'nota_criatividade': forms.TextInput(attrs={'class': 'form-control'}),
            'nota_performance': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control'}),
        }
    







