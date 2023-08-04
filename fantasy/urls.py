from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'fantasy'

urlpatterns = [
    path('', views.candidatos, name='candidatos' ),
    path('julgamento/<int:id>', views.julgamento_get, name='julgamento_get'),
    path('julgamento_post/', views.julgamento_post, name='julgamento_post'),
    path('relatorio/', views.relatorio, name='relatorio')
    #path('makeyourself/', include('makeyourself.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 