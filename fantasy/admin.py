from django.contrib import admin
from .models import Participante, Jurado, Julgamento


# Register your models here.
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'personagem', 'email', 'telefone']
    search_fields = ('nome',)
    ordering = ('nome',)

admin.site.register(Participante, ParticipanteAdmin)

class JuradoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Jurado, JuradoAdmin)


class JulgamentoAdmin(admin.ModelAdmin):
    list_display = ['participante', 'jurado', 'nota_estetica', 'nota_criatividade', 'nota_performance', 'nota_final', 'observacao']
    ordering = ('participante', 'jurado')

admin.site.register(Julgamento, JulgamentoAdmin)