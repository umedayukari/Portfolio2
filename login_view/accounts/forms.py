from django import forms
#from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
#from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()

class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    sex =forms.CharField(label='性別')
    date_of_birth = forms.DateField(label='生年月日')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model =Users
        fields = ('username','email','sex','date_of_birth','password')
    
    
        
class EmailLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス', required=True)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput, required=True)
  
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError("無効なメールアドレスまたはパスワードです。")
            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
  
  
  # class Meta:
   #model = Users
   #fields = ['email', 'password']
   #labels = {'email': 'メールアドレス', 'password': 'パスワード'}

   #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['username'].widget.attrs['disabled'] = True
     #   self.fields['username'].required = False
    
   #def clean(self):
    #    cleaned_data = super().clean()
     #   email = cleaned_data.get('email')
      #  password = cleaned_data.get('password')
        
      #  if not email or not password:
       #     raise forms.ValidationError("Both email and password are required.")
    
      #  return cleaned_data
    
    
    