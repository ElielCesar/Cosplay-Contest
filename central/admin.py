from django.contrib import admin
from .models import *
# Register your models here.

class Fantasy_Admin(admin.ModelAdmin):
    list_display = ('id','usuario','nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal')
    
    
class Makeyourself_Admin(admin.ModelAdmin):
    list_display = ('id','usuario','nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal')


class Jurado_Admin(admin.ModelAdmin):
     list_display = ('id','nome_completo', 'email', 'telefone', 'foto')
     
     
class Organizadores_Admin(admin.ModelAdmin):
     list_display = ('id','nome_completo', 'email', 'telefone', 'foto')
     
     
class Apoiadores_Admin(admin.ModelAdmin):
     list_display = ('id','nome_completo', 'email', 'telefone', 'foto')
     
class Julgamento_Fantasy_Admin(admin.ModelAdmin):
     list_display = ('id', 'jurado', 'participante_fantasy', 'nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_sustentabilidade', 'observacao')

class Julgamento_Makeyourself_Admin(admin.ModelAdmin):
     list_display = ('id', 'jurado', 'participante_makeyourself', 'nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_sustentabilidade', 'observacao')


# register
admin.site.register(Fantasy, Fantasy_Admin)
admin.site.register(MakeYourSelf, Makeyourself_Admin)
admin.site.register(Jurado, Jurado_Admin)
admin.site.register(Apoiadores, Apoiadores_Admin)
admin.site.register(Organizadores, Organizadores_Admin)
admin.site.register(Julgamento, Julgamento_Fantasy_Admin)
admin.site.register(Julgamento_MakeYourSelf, Julgamento_Makeyourself_Admin)