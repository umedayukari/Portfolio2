from django import forms
from .models import Themes, Comments, Opponent

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='お相手の名前')

    class Meta:
        model = Themes
        fields = ('title',)
        
class OpponentForm(forms.ModelForm):
    class Meta:
        model = Opponent
        fields = ['date', 'sex', 'name', 'anniversary_details'] 

       
