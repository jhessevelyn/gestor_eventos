from django.contrib import admin 
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from eventos.views import EventoViewSet, ParticipanteViewSet, AtividadeViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView 
 
router = DefaultRouter()
router.register(r'eventos', EventoViewSet) 
router.register(r'participantes', ParticipanteViewSet) 
router.register(r'atividades', AtividadeViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)), 
    path('api/token/', obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]