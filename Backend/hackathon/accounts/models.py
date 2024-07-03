from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from Course.models import Course

# Create your models here.

class UserCustom(AbstractUser):


    niveau = models.CharField(max_length=25, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Changer le nom personnalisé ici
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Changer le nom personnalisé ici
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )    
    
    def __str__(self):
        return self.username
    
    
