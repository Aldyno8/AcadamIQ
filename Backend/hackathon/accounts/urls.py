from django.urls import path 
from accounts import views 


urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path('reset_password/', views.PasswordRestView.as_view(), name='reset_password'),
    path('reset_confirm/', views.PassWordResetConfirm.as_view(), name='reset_confirm'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
]
