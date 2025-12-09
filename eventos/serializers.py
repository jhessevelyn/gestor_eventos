from rest_framework import serializers 
from .models import Evento, Participante, Atividade 

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__' 

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'

class EventoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nome', 'descricao', 'data_inicio', 'data_fim', 'local']

class AtividadeNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'titulo', 'descricao', 'hora_inicio', 'hora_fim', 'tipo', 'responsavel']

class InscricaoSerializer(serializers.Serializer):
    participante = serializers.PrimaryKeyRelatedField(
        queryset = Participante.objects.all()
    )

