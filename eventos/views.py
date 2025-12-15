from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Evento, Participante, Atividade 
from .serializers import EventoSerializer, ParticipanteSerializer, AtividadeSerializer
from .serializers import EventoNestedSerializer, AtividadeEventoSerializer, InscricaoSerializer, ResponsavelSerializer, AtividadeCreateSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
 
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer

    # GET - endpoint: /eventos{id}/participantes
    @action(detail=True, methods=['get'], serializer_class=InscricaoSerializer)
    def participantes(self, request, pk=None):
        evento = self.get_object()
        serializer = ParticipanteSerializer(evento.participantes.all(), many=True)
        return Response(serializer.data)
    
    # POST - endpoint: /eventos{id}/participantes
    @participantes.mapping.post
    def inscrever_participante(self, request, pk=None):
        evento = self.get_object()

        insc_serializer = InscricaoSerializer(data=request.data)
        insc_serializer.is_valid(raise_exception=True  )

        participante = insc_serializer.validated_data['participante']

        if evento.participantes.filter(pk=participante.pk).exists():
            return Response({"detail": "Participante já inscrito neste evento."},
                            status=status.HTTP_200_OK)

        evento.participantes.add(participante)
        return Response({"detail": "Participante inscrito com sucesso no evento."},
                        status=status.HTTP_201_CREATED)

    # GET - endpoint: /eventos/{id}/atividades
    @action(detail=True, methods=['get'], serializer_class=AtividadeCreateSerializer)
    def atividades(self, request, pk=None):
        evento = self.get_object()
        serializer = AtividadeEventoSerializer(evento.atividades.all(), many=True)  
        return Response(serializer.data)
        
    # POST - enpoint: /eventos/{id}/atividades
    @atividades.mapping.post
    def criar_atividades(self, request, pk=None):
        evento = self.get_object()
        data = request.data

        responsavel_id = data.get("responsavel")
        responsavel = get_object_or_404(Participante, pk=responsavel_id)

        atividade = Atividade.objects.create(
            evento = evento,
            titulo = data["titulo"],
            descricao = data.get("descricao", ""),
            hora_inicio = data["hora_inicio"],
            hora_fim = data["hora_fim"],
            tipo = data["tipo"],
            responsavel = responsavel
        )
        return Response(AtividadeCreateSerializer(atividade).data, status=201)
    
    # GET - endpoint: /eventos/{id}/dashboard
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        evento = self.get_object()
        atividade_qs = evento.atividades.select_related('responsavel').all()
        participantes_qs = evento.participantes.all()

        evento_data = EventoNestedSerializer(evento).data
        atividade_data = AtividadeEventoSerializer(atividade_qs, many=True).data
        participantes_data = ParticipanteSerializer(participantes_qs, many=True).data

        payload = {
            'evento': evento_data,
            'atividades': atividade_data,
            'participantes': participantes_data
        }
        return Response(payload, status=status.HTTP_200_OK)
    
    
class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all() 
    serializer_class = ParticipanteSerializer


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all() 
    serializer_class = AtividadeSerializer

    # GET - endpoint: /atividades/{id}/responsavel
    @action(detail=True, methods=['get'], serializer_class=ResponsavelSerializer)
    def responsavel(self, request, pk=None):
        atividade = self.get_object()
        serializer = ParticipanteSerializer(atividade.responsavel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST - endpoint: /atividades/{id}/responsavel
    @responsavel.mapping.put
    def set_responsavel(self, request, pk=None):
        atividade = self.get_object()

        r_serializer = ResponsavelSerializer(data=request.data)
        r_serializer.is_valid(raise_exception=True)
        participante = r_serializer.validated_data['participante']

        if atividade.responsavel and atividade.responsavel.pk == participante.pk:
            return Response(status=status.HTTP_204_NO_CONTENT)

        atividade.responsavel = participante
        atividade.save()

        return Response(status=status.HTTP_204_NO_CONTENT)