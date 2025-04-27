from django.db import models
from patients.models import Patient
from facturation.models import Facture

# Create your models here.
class Paiement(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    mode_paiement = models.CharField(max_length=50)  # e.g., 'Carte', 'Espèces', 'Chèque'
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Paiement de {self.montant} le {self.date_paiement}"
    

class SortieFonds(models.Model):
    
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_sortie = models.DateTimeField(auto_now_add=True)
    motif = models.TextField()
    responsable = models.CharField(max_length=100)  # Nom de la personne responsable de la sortie

    def __str__(self):
        return f"Sortie de {self.montant} le {self.date_sortie} pour {self.motif} par {self.responsable}"