from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

# Create your models here.
class Participante(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    personagem = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=50, blank=False, null=False)
    imagem = models.ImageField(upload_to='fantasy/')


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'


class Jurado(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nome


class Julgamento(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.DO_NOTHING, blank=False, null=False)
    jurado = models.ForeignKey(Jurado, on_delete=models.DO_NOTHING, blank=False, null=False)
    nota_estetica = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)])
    nota_criatividade = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)])
    nota_performance = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)]) 
    nota_final = models.IntegerField(validators=[MaxValueValidator(40), MinValueValidator(4)])
    observacao = models.CharField(max_length=300)

    # acrescentar imagem do candidato no Django Admin





