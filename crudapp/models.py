from django.db import models

# Create your models here.
class Poste(models.Model):
    titre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.titre

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE)