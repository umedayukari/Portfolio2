from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegistForm
from .forms import EmailAuthenticationForm
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm
    success_url = reverse_lazy('accounts:login')
    
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('accounts:login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = EmailAuthenticationForm
    
    def form_valid(self, form):
        # フォームがバリデーションを通過した場合の処理
        print("Form is valid")
        print("POST data:", self.request.POST)
        return super().form_valid(form)

    def form_invalid(self, form):
        # フォームがバリデーションエラーとなった場合の処理
        print("Form is invalid")
        print("Form errors:", form.errors)
        return super().form_invalid(form)
    
    
class UserLogoutView(LogoutView):
    template_name = 'logout.html'   
    



