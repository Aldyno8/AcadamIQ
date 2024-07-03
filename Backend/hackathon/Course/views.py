from django.shortcuts import get_object_or_404, render
import google.generativeai as genai, json
from Positioning.models import UserScore
from .models import  Course
from django.views import View
genai.configure(api_key='AIzaSyCCxaDqzURX6KS4Ai01U-iop7_U2jKjuNw')

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


class Course(View):
    def get(self, request):
        score = get_object_or_404(UserScore, user=request.user)
        
        chat_session = model.start_chat(history=[])
        Demande = ('lecons complets et détaillé sur le l\'algorithme pour un individu debutant avec ce schema : [{ "sous_titre": str, "contenu_du_cours": str, "remarque": str}]')    
        response = chat_session.send_message(Demande)
        answer_text = response.text
        cours = answer_text.replace("***", "<br>")
        cours = answer_text.replace("**", "<br>")
        cours = answer_text.replace("*", "<br>")
        lesson = json.loads(cours)
        
    
        return render(request, 'course.html', {'score': score, 'lesson': lesson})
