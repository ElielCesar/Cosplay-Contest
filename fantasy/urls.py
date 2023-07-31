from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.candidatos, name='candidatos' ),
    path('julgamento/', views.julgamento, name='julgamento'),
    #path('makeyourself/', include('makeyourself.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 