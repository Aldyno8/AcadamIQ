from django.contrib.auth import views
# Create your views here.

class LoginView(views.LoginView):
    template_name = 'login.html'
    success_url = 'home'
    
class LogoutView(views.LogoutView):
    template_name = 'logout.html'
    success_url = 'login'
    
class PasswordRestView(views.PasswordResetView):
    template_name = 'reset_password.html'
    success_url = 'reset_confirm'
    
class PassWordResetConfirm(views.PasswordResetConfirmView):
    template_name = 'confirm_reset.html'
    success_url = 'reset_complete'
    
    
class ChangePassword(views.PasswordChangeView):
    template_name ='password_change.html'
    success_url =  'password_change_done'

    
class ChangeDone(views.PasswordChangeDoneView):
    template_name = 'change_done.html'
    
    
    
