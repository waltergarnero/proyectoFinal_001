"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include # importamos include  para poder trabajar con las urls de noticias
#from apps.noticias import views  # Importamos la app noticias
from . import views 

from django.conf import settings
from django.conf.urls.static import static

# URL Principal
urlpatterns = [
    #path('',views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    #path para la url de la vista de home 
    #path('',views.inicio1, name='inicio1'),
    #path('home',views.inicio1, name='inicio1'),
    path('',views.inicio2, name='inicio2'),
    path('inicio2',views.inicio2, name='inicio2'),
    # recibe 3 parametros, funcion , y el nombre 
    #path de nosotros
  
    path('nosotros1',views.nosostros1,name='nosotros1'),    
    path('nosotros2',views.nosostros2,name='nosotros2'),
   
    # ----------- URL APP NOTICIAS ----------
    path('noticias/',include('apps.noticias.urls')) ,

     # ----------- URL APP CONTACTO----------
    path('contactos/',include('apps.contactos.urls')) ,   
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
