from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Evento, Participante, Atividade 
from .serializers import EventoSerializer, ParticipanteSerializer, AtividadeSerializer
from .serializers import AtividadeNestedSerializer, InscricaoSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
 
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer

    @action(detail=True, methods=['get', 'post'], serializer_class=InscricaoSerializer)
    def participantes(self, request, pk=None):
        evento = self.get_object()

        if request.method == 'GET':
            serializer = ParticipanteSerializer(evento.participantes.all(), many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            insc_serializer = InscricaoSerializer(data=request.data)
            insc_serializer.is_valid(raise_exception=True)

            participante = insc_serializer.validated_data['participante']

            if evento.participantes.filter(pk=participante.pk).exists():
                return Response(ParticipanteSerializer(participante).data, status=status.HTTP_200_OK)

            evento.participantes.add(participante)
            return Response(ParticipanteSerializer(participante).data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['get', 'post'], serializer_class=AtividadeNestedSerializer)
    def atividades(self, request, pk=None):
        evento = self.get_object()

        if request.method == 'GET':
            serializer = AtividadeNestedSerializer(evento.atividades.all(), many=True)  
            print(serializer.data)
            return Response(serializer.data)
        
        if request.method == 'POST':
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
            return Response(AtividadeNestedSerializer(atividade).data, status=201)
    
    
class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all() 
    serializer_class = ParticipanteSerializer


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all() 
    serializer_class = AtividadeSerializer

    @action(detail=True, methods=['get', 'put'],serializer_class =  ParticipanteSerializer)
    def responsavel(self, request, pk=None):
        atividade = self.get_object()
        if request.method == 'GET':
             serializer = ParticipanteSerializer(atividade.responsavel)
        return Response(serializer.data)

