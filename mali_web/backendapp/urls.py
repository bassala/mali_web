from django.urls import path
from . import views
from .views import get_region_data

urlpatterns = [
    path('afficher_carte/', views.afficher_carte, name='afficher_carte'),
    path('get_region_data/', get_region_data, name='get_region_data'),
]
