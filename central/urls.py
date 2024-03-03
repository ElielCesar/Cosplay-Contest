from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'central'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inscrever/', InscreverView.as_view(), name='inscrever'),
    
    # urls para CBV Fantasy
    path('inscritos_fantasy/', InscritosFantasyView.as_view(), name='inscritos_fantasy'),
    path('inscrever_fantasy/', InscreverFantasyView.as_view(), name='inscrever_fantasy'),
    path('deletar_fantasy/<int:pk>/',DeletarFantasyView.as_view() ,name='deletar_fantasy'),
    
    # urls para CBV Fantasy
    path('inscritos_makeyourself/', InscritosMakeYourSelfView.as_view(), name='inscritos_makeyourself'),
    path('inscrever_makeyourself/', InscreverMakeYourSelfView.as_view(), name='inscrever_makeyourself'),
    path('deletar_makeyourself/<int:pk>/',DeletarMakeYourSelfView.as_view() ,name='deletar_makeyourself'),
    
    # urls para Julgamento
    path('julgamento/', JulgamentoView.as_view(), name='julgamento'),
    path('julgamento_fantasy/<int:inscrito_id>/', JulgamentoFantasyView.as_view(), name='julgamento_fantasy'),
    #path('julgamento_makeyourself/', julgamento_makeyourself, name='julgamento_makeyourself'),
    
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 