from django.contrib import admin
from .models import  Course

# Register your models here.
  
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('niveau', 'Contenu')
    search_fields = ('niveau',)

admin.site.register(Course, CourseAdmin)


