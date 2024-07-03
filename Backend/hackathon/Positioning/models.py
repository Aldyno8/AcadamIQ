from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modeles qui va gérer les question 
class Question(models.Model):
    question = models.TextField()
    
    def __str__(self):
        return self.question
 
# Modeles qui va gérer les choix multiples pour chaque question  
class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    
class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.niveau
    
    

    