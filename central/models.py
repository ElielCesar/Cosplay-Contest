from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.db.models import Sum


class Jurado(models.Model):
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=21, blank=False, null=False)
    foto = models.ImageField(upload_to='jurados/', null=True)
    
    
class Organizadores(models.Model):
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=21, blank=False, null=False)
    foto = models.ImageField(upload_to='organizadores/', null=True)


class Apoiadores(models.Model):
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=21, blank=False, null=False)
    foto = models.ImageField(upload_to='apoiadores/', null=True)   
    
    def get_absolute_url(self):
        return reverse('apoiador-detalhe', kwargs={'pk': self.pk})

# Models
class MakeYourSelf(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=21, blank=False, null=False)
    personagem = models.CharField(max_length=200, blank=False, null=False)
    imagem_principal = models.ImageField(upload_to='makeyourself/')
    
    def __str__(self):
        return f'{self.nome_completo}'
    
    
class Fantasy(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=21, blank=False, null=False)
    personagem = models.CharField(max_length=200, blank=False, null=False)
    imagem_principal = models.ImageField(upload_to='fantasy/')
    
    def __str__(self):
        return f'{self.nome_completo}'
           
class Julgamento(models.Model):
    participante_fantasy = models.ForeignKey(Fantasy, on_delete=models.CASCADE, blank=True, null=True, related_name='julgamentos_fantasy')
    jurado = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='julgamentos')
    nota_estetica = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_criatividade = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_performance = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_sustentabilidade = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    observacao = models.CharField(max_length=500, blank=True, null=True)
    

class Julgamento_MakeYourSelf(models.Model):
    participante_makeyourself = models.ForeignKey(MakeYourSelf, on_delete=models.CASCADE, blank=True, null=True, related_name='julgamentos_makeyourself')
    jurado = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name='julgamentos_makeyourself')
    nota_estetica = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_criatividade = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_performance = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    nota_sustentabilidade = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    observacao = models.CharField(max_length=500, blank=True, null=True)
    