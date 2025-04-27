from django.db import models

# Create your models here.
class Patient(models.Model):


    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"

    

