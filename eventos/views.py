from rest_framework import viewsets 
from .models import Evento, Participante, Atividade 
from .serializers import EventoSerializer, ParticipanteSerializer, AtividadeSerializer
from django_filters.rest_framework import DjangoFilterBackend
 
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer 

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all() 
    serializer_class = ParticipanteSerializer
    filter_backends = [DjangoFilterBackend] 
 
    filterset_fields = ['nome', 'email', 'celular', 'tipo']

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all() 
    serializer_class = AtividadeSerializer 