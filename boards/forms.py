from django import forms
from .models import Themes, Comments

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='プレセントの目的・用途')

    class Meta:
        model = Themes
        fields = ('title',)