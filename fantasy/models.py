from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# classe abstrata - campos comuns devem sem implementados aqui
class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome


class Participante(Pessoa):
    
    personagem = models.CharField(max_length=200, blank=False, null=False)
    imagem = models.ImageField(upload_to='fantasy/')


class Jurado(Pessoa):

    def __str__(self):
        return self.nome


class Julgamento(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.DO_NOTHING, blank=False, null=False)
    jurado = models.ForeignKey(Jurado, on_delete=models.DO_NOTHING, blank=False, null=False)
    nota_estetica = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)])
    nota_criatividade = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)])
    nota_performance = models.IntegerField(validators=[ MaxValueValidator(10), MinValueValidator(1)]) 
    nota_final = models.IntegerField(validators=[MaxValueValidator(40), MinValueValidator(4)], blank=True, null=True)
    observacao = models.CharField(max_length=300, blank=True, null=True)


@receiver(post_save, sender=Julgamento)
def somar_notas(sender, instance, created, **kwargs):
    if created:
        instance.nota_final = instance.nota_estetica + instance.nota_criatividade + instance.nota_performance
        instance.save(update_fields=['nota_final'])



