##########################################  ces deux lignes pour metre d'afficher 
############ mes media sur le navigateur
from django.conf import settings
from django.conf.urls.static import static
##########################################
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('backendapp.urls')),
    path('admin/', admin.site.urls),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # cette ligne
     # il se trouve dans settings et le dossier media dans le projet 
