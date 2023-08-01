from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('fantasy.urls')),
    path('admin/', admin.site.urls),
    path('fantasy/', include('fantasy.urls')),
    #path('makeyourself/', include('makeyourself.urls')),
]

admin.site.site_header = 'Cosplay Contest'  
# Nome que aparece no titulo da aba do navegador
admin.site.site_title = 'Cosplay Contest'  
# Nome no lado esquerdo do painel django admin
admin.site.index_title = 'Cosplay Contest'                         
