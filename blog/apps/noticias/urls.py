from django.urls import path
from . import views

app_name = 'noticias'

# URL de app noticias
urlpatterns = [
    path('',views.inicio,name='inicio')
    ]
