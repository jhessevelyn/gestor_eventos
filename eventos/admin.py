from django.contrib import admin
from .models import Evento, Participante, Atividade
from rest_framework.authtoken.models import Token

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome'] 
    search_fields = ['nome'] 

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'celular', 'tipo'] 
    search_fields = ['nome', 'email'] 
    list_filter = ['tipo'] 
    admin.site.register(Token)

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao'] 
    search_fields = ['titulo', 'descricao'] 
    list_filter = ['titulo'] 

admin.site.register(Atividade, AtividadeAdmin)
