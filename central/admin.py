from django.contrib import admin
from .models import *
# Register your models here.

class Fantasy_Admin(admin.ModelAdmin):
    list_display = ('usuario','nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal')
    
    
class Makeyourself_Admin(admin.ModelAdmin):
    list_display = ('usuario','nome_completo', 'email', 'telefone', 'personagem', 'imagem_principal')


class Jurado_Admin(admin.ModelAdmin):
     list_display = ('usuario','nome_completo', 'email', 'telefone', 'foto')
     
     
class Organizadores_Admin(admin.ModelAdmin):
     list_display = ('nome_completo', 'email', 'telefone', 'foto')
     
     
class Apoiadores_Admin(admin.ModelAdmin):
     list_display = ('nome_completo', 'email', 'telefone', 'foto')

# register
admin.site.register(Fantasy, Fantasy_Admin)
admin.site.register(MakeYourSelf, Makeyourself_Admin)
admin.site.register(Jurado, Jurado_Admin)
admin.site.register(Apoiadores, Apoiadores_Admin)
admin.site.register(Organizadores, Organizadores_Admin)