from django.db import models
from actes.models import Acte
from medicaments.models import Medicament

# Create your models here.
class Consultation(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(auto_now_add=True)
    motif = models.TextField()
    traitement = models.TextField(blank=True, null=True)
    actes_recommandes = models.ManyToManyField(Acte, related_name='consultations')
    ordonances = models.ManyToManyField(Medicament, related_name='consultations')
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Consultation de {self.patient} le {self.date_consultation}"