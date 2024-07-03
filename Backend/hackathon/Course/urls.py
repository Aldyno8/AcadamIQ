from django.urls import path
from .views import Course

urlpatterns = [
    path('lesson/', Course.as_view(), name='Lesson_list')
]


