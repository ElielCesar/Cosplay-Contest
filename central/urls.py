from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'central'
urlpatterns = [
    path('', home, name='home'),
    path('inscrever/', inscrever, name='inscrever'),
    path('inscrever_fantasy/', inscrever_fantasy, name='inscrever_fantasy'),
    path('inscrever_makeyourself/', inscrever_makeyourself, name='inscrever_makeyourself'),
    path('buscar_inscritos/', buscar_inscritos, name='buscar_inscritos'),
    # urls para CBVs Jurados
    path('criar_jurado/', JuradosCreateView.as_view(), name='criar_jurado'),
    path('listar_jurados/', JuradosListView.as_view(), name='listar_jurados'),
    path('editar_jurado/<int:pk>/', JuradosUpdateView.as_view(), name='editar_jurado'),
    path('deletar_jurado/<int:pk>/', JuradosDeleteView.as_view(), name='deletar_jurado'),
    
    # urls para CBVs Organizador
    path('criar_organizador/', OrganizadoresCreateView.as_view(), name='criar_organizador'),
    path('listar_organizadores/', OrganizadoresListView.as_view(), name='listar_organizadores'),
    path('editar_organizador/<int:pk>/', OrganizadoresUpdateView.as_view(), name='editar_organizador'),
    path('deletar_organizador/<int:pk>/', OrganizadoresDeleteView.as_view(), name='deletar_organizador'),
    
    # urls para CBVs Apoiador
    path('criar_apoiador/', ApoiadoresCreateView.as_view(), name='criar_apoiador'),
    path('listar_apoiadores/', ApoiadoresListView.as_view(), name='listar_apoiadores'),
    path('editar_apoiador/<int:pk>/', ApoiadoresUpdateView.as_view(), name='editar_apoiador'),
    path('deletar_apoiador/<int:pk>/', ApoiadoresDeleteView.as_view(), name='deletar_apoiador'),
    path('julgamento/', julgamento, name='julgamento'),
    path('julgamento_fantasy/', julgamento_fantasy, name='julgamento_fantasy'),
    path('julgamento_makeyourself/', julgamento_makeyourself, name='julgamento_makeyourself'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 