from django.db import models
from Positioning.models import UserScore


# Create your models here.
# Modeles qui va gérer les chapitres à aborder dans le cours vis-à-vis du score
class Course(models.Model):
    niveau = models.ForeignKey(UserScore, on_delete=models.CASCADE)
    Contenu = models.TextField()
   
    def __str__(self):
        return self.niveau
