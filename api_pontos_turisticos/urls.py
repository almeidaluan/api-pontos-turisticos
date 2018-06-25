from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet 
from atracoes.api.viewsets import AtracoesViewSet
from avaliacao.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register('pontoturistico',PontoTuristicoViewSet,base_name='PontoTuristico') # quando se usa def get_queryset voce tem que definir o basename com name do model
router.register('Atracoes',AtracoesViewSet)
router.register('Avaliacoes',AvaliacaoViewSet)
router.register('Comentario',ComentarioViewSet)
router.register('Enderecos',EnderecoViewSet,base_name='Endereco')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
