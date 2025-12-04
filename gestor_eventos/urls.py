from django.contrib import admin 
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from eventos.views import EventoViewSet, ParticipanteViewSet, AtividadeViewSet
 
router = DefaultRouter()
router.register(r'eventos', EventoViewSet) 
router.register(r'participantes', ParticipanteViewSet) 
router.register(r'atividades', AtividadeViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)), 
]