from django.shortcuts import render, redirect, get_object_or_404
from .models import Question,Choice, UserScore
from django.views import View
from Course.models import Course
import google.generativeai as genai
import re, json
 




genai.configure(api_key='AIzaSyCCxaDqzURX6KS4Ai01U-iop7_U2jKjuNw')

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


 # vue pour la liste des question
class Quiz(View):
   def get(self, request):
       question = Question.objects.all()
       return render(request,'positioning.html', {'question':question})
   
class PositioningView(View):
    def post(self, request, format=None):
        score = 0
        for question in Question.objects.all():
            answer = request.POST.get(f'question_{question.id}')
    
        #verifie si l'utilisateur a entreé les réponses
        if answer is not None:
            choice = Choice.objects.get(id=answer)
            if choice.is_correct:
                score += 1
        
        
        
        # Attrbution de niveau et et affichage des theme a aborde
        
        if score < 3:
            level = 'Debutant'
        elif score < 5:
            level = 'Intermediaire'
        elif score < 7:
            level = 'Avance'
        elif score < 9:
            level = 'Expert'
        else:
            level = 'Maitre'    
            
        
        UserScore.objects.create(user=request.user, niveau = level)
        return redirect ('Positioning_test')
        
        
class QuizResult(View):
    def get(self, request):
        score = get_object_or_404(UserScore, user=request.user)
        
        return render(request, 'resultat.html', {'level':score})


        