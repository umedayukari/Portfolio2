from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    sex =forms.CharField(label='性別')
    date_of_birth = forms.DateField(label='生年月日')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    
    class Meta:
        model =Users
        fields = ['username','email','sex','date_of_birth','password']
    
    
        
class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='メールアドレス', required=True)

    class Meta:
        model = Users
        fields = ['email', 'password']
        labels = {'email': 'メールアドレス', 'password': 'パスワード'}
    
    
    
    
    