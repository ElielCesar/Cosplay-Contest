from django.contrib import admin
from .models import Participante, Jurado, Julgamento


# Register your models here.
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'personagem', 'email', 'telefone']
    search_fields = ('nome',)
    ordering = ('nome',)

admin.site.register(Participante, ParticipanteAdmin)