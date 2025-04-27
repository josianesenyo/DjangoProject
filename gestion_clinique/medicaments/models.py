from django.db import models

# Create your models here.
class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()
    date_expiration = models.DateField()
    
    def __str__(self):
        return self.nom
