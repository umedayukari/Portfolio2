from django import forms
from .models import Themes, Comments, Opponent
from .models import AnniversaryRecords


class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='お相手の名前', max_length=100)

    class Meta:
        model = Themes
        fields = ('title',)
        
class OpponentForm(forms.ModelForm):
    date = forms.DateField(label='日付')
    sex = forms.CharField(label='性別')
    name = forms.CharField(label='名前')
    anniversary_details = forms.CharField(label='記念日の詳細', widget=forms.Textarea)
    
    class Meta:
        model = Opponent
        fields = ['date', 'sex', 'name', 'anniversary_details'] 


class AnniversaryRecordForm(forms.ModelForm):
    class Meta:
        model = AnniversaryRecords
        fields = [
            'date', 
            'opponent', 
            'relationships', 
            'purpose', 
            'present', 
            'present_type',
            'range_of_amounts',
            'amount_of_money',
            'photo',
            'memories',
            'self_assessment', 
            'improvements'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'memories': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            'self_assessment': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            'improvements': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            # その他のフィールドも必要に応じてここに追加してください
        }
        labels = {
            'date': '日付',
            'opponent': 'お相手のID',
            'relationships': '関係性',
            'purpose': '目的',
            'present': 'プレゼント',
            # その他のフィールドのラベルもここに追加してください
        }
       
