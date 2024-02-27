from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('autenticacao.urls')),
    path('home/', include('central.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Cosplay Contest'  
# Nome que aparece no titulo da aba do navegador
admin.site.site_title = 'Cosplay Contest'  
# Nome no lado esquerdo do painel django admin
admin.site.index_title = 'Cosplay Contest'                         
