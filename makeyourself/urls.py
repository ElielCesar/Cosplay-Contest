from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'makeyourself'

urlpatterns = [
    path('', views.candidatos, name='candidatos' ),
    path('julgamento/<int:id>', views.julgamento_get, name='julgamento_get'),
    path('julgamento_post/', views.julgamento_post, name='julgamento_post'),
    path('relatorio/', views.relatorio, name='relatorio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 






