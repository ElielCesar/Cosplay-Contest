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
    path('jurados/', jurados, name='jurados'),
    path('organizadores/', organizadores, name='organizadores'),
    path('apoiadores/', apoiadores, name='apoiadores'),
    path('julgamento/', julgamento, name='julgamento'),
    path('julgamento_fantasy/', julgamento_fantasy, name='julgamento_fantasy'),
    path('julgamento_makeyourself/', julgamento_makeyourself, name='julgamento_makeyourself'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 