from rest_framework import serializers 
from .models import Evento, Participante, Atividade 

class ParticipanteSerializer(serializers.ModelSerializer):
    """
    Serializer genérico para CRUD de Participante.
    """
    class Meta:
        model = Participante
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    """
    Serializer genérico para CRUD de Evento.
    """
    class Meta:
        model = Evento
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    """
    Serializer genérico para CRUD de Atividade.
    """
    class Meta:
        model = Atividade
        fields = '__all__'

class InscricaoSerializer(serializers.Serializer):
    """
    Serializer para validar os dados para inscrição (POST) de um participante em um evento.
    """
    participante = serializers.PrimaryKeyRelatedField(
        queryset = Participante.objects.all()
    )

class AtividadeCreateSerializer(serializers.ModelSerializer):
    """
    Serializer responsável por criar atividades vinculadas a um evento
    """
    responsavel = serializers.PrimaryKeyRelatedField(
        queryset = Participante.objects.all()
    )

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'hora_inicio', 'hora_fim', 'tipo', 'responsavel']


class AtividadeEventoSerializer(serializers.ModelSerializer):
    """
    Serializer responsável pela representação de atividades no contexto de um evento.
    """
    responsavel = ParticipanteSerializer(read_only=True)

    class Meta:
        model = Atividade
        fields = ['id', 'titulo', 'descricao', 'hora_inicio', 'hora_fim', 'tipo', 'responsavel']


class InscricaoSerializer(serializers.Serializer):
    """
    Serializer responsável por validar a inscrição de um participante em um evento.
    """
    participante = serializers.PrimaryKeyRelatedField(
        queryset = Participante.objects.all()
    )

class ResponsavelSerializer(serializers.Serializer):
    """
    Serializer responsável por validar a atribuição ou alteração do responsável de uma atividade.
    """
    # campo para o PUT (escolha por id)
    participante = serializers.PrimaryKeyRelatedField(
        queryset=Participante.objects.all(),
        write_only=True,
        allow_null=True
    )


class EventoNestedSerializer(serializers.ModelSerializer):
    """
    Serializer responsável pela representação resumida de um evento (dashboard).
    """
    class Meta:
        model = Evento
        fields = ['id', 'nome', 'descricao', 'data_inicio', 'data_fim', 'local']