from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_actes, name='liste_actes'),
    path('ajouter/', views.ajouter_acte, name='ajouter_acte'),
    path('modifier/<int:acte_id>/', views.modifier_acte, name='modifier_acte'),
    path('supprimer/<int:acte_id>/', views.supprimer_acte, name='supprimer_acte'),
]
