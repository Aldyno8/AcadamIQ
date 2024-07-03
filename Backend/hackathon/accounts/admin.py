from django.contrib import admin
from .models import UserCustom

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    models = UserCustom
    list_display = ('username', 'email', 'niveau') 
    
admin.site.register(UserCustom, UserAdmin)