from rest_framework import viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Evento, Participante, Atividade 
from .serializers import EventoSerializer, ParticipanteSerializer, AtividadeSerializer
from django_filters.rest_framework import DjangoFilterBackend
 
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer 

    @action(detail=True, methods=['get'])
    def atividades(self, request, pk=None):
        evento = self.get_object()
        serializer = AtividadeSerializer(evento.atividades.all(), many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def participantes(self, request, pk=None):
        evento = self.get_object()
        serializer = ParticipanteSerializer(evento.participantes.all(), many=True)
        return Response(serializer.data)

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all() 
    serializer_class = ParticipanteSerializer
    
    

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all() 
    serializer_class = AtividadeSerializer 

    @action(detail=True, methods=['get'])
    def responsavel(self, request, pk=None):
        atividade = self.get_object()
        serializer = ParticipanteSerializer(atividade.responsavel)
        return Response(serializer.data)