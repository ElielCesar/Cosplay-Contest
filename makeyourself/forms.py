from django import forms
from .models import Participante, Jurado, Julgamento
from django.forms import Select


class Form_Julgamento(forms.ModelForm):
    class Meta:
        model = Julgamento
        fields = ['participante', 'jurado', 'nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_sustentabilidade', 'observacao']

        widgets = {
            'participante': Select(attrs={'class': 'form-control mb-2'}),
            'jurado': Select(attrs={'class': 'form-control mb-2'}),
            'nota_estetica': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'nota_criatividade': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'nota_performance': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'nota_sustentabilidade': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }
    







