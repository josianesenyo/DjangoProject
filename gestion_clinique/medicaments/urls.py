from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_medicaments, name='liste_medicaments'),
    path('ajouter/', views.ajouter_medicament, name='ajouter_medicament'),
    path('modifier/<int:pk>/', views.modifier_medicament, name='modifier_medicament'),
    path('supprimer/<int:pk>/', views.supprimer_medicament, name='supprimer_medicament'),
]
