from django.db import models
from patients.models import Patient
from consultations.models import Consultation

# Create your models here.
class Facture(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    numero_facture = models.CharField(max_length=10, unique=True, blank=True, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_emission = models.DateTimeField(auto_now_add=True)
    payee = models.BooleanField(default=False)
    date_paiement = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Facture {self.numero_facture} - Patient: {self.patient.nom} {self.patient.prenom} - Montant: {self.montant}"
    
    def save(self, *args, **kwargs):
        if not self.numero_facture:
            dernier_id = Facture.objects.all().count() + 1
            self.numero_facture = f"#{dernier_id:04d}"
        super().save(*args, **kwargs)