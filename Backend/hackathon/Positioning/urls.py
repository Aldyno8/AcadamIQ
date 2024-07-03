from django.urls import path
from .views import  PositioningView, Quiz, QuizResult

urlpatterns = [
    path('question/', Quiz.as_view(), name='Question_list'),
    path('evaluation/', PositioningView.as_view(), name='Positioning'),
    path('resultat/', QuizResult.as_view(), name='Positioning_test')
]
