from django.contrib import admin
from .models import Question, Choice, UserScore

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question',)
    
class ScoreAdmin(admin.ModelAdmin):
    model = UserScore
    list_display = ('niveau',)
    
    
admin.site.register( Question, QuestionAdmin)
admin.site.register(UserScore, ScoreAdmin)