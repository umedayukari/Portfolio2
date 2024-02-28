from django import forms
from .models import Themes, Comments, Opponent
from .models import AnniversaryRecords

PRESENT_CHOICES = [
    ('ornament', '装飾品'),
    ('clothes', '衣類'),
    ('food', '食べ物'),
    ('trip', '旅行'),
    ('letter', '手紙'),
    ('other', 'その他'),
]

AMOUNT_RANGE_CHOICES = [
    ('0-500', '¥0 - ¥500'),
    ('501-1000', '¥501 - ¥1,000'),
    ('1001-5000', '¥1,001 - ¥5,000'),
    ('5001-10000', '¥5,001 - ¥10,000'),
    ('10001-30000', '¥10,001 - ¥30,000'),
    ('30001-50000', '¥30,001 - ¥50,000'),
    ('50001+', '¥50,001以上'),
    ('unknown', '不明'),
]


class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='お相手の名前', max_length=100)

    class Meta:
        model = Themes
        fields = ('title',)
        
class OpponentForm(forms.ModelForm):
    date = forms.DateField(
        label='日付',
        widget=forms.DateInput(attrs={'type': 'date'})
        )
    sex = forms.CharField(label='性別')
    name = forms.CharField(label='名前')
    anniversary_details = forms.CharField(label='記念日の詳細', max_length=100)
    
    class Meta:
        model = Opponent
        fields = ['date', 'sex', 'name', 'anniversary_details'] 


class AnniversaryRecordForm(forms.ModelForm):
    opponent = forms.ModelChoiceField(
        queryset=Opponent.objects.all(),  # Opponent モデルの全オブジェクトを選択肢として取得
        label='お相手の名前',  # ラベルを「お相手の名前」に変更
        to_field_name='name'  # ここで 'name' は Opponent モデルの名前フィールドを指します
    )
    
    present_type = forms.ChoiceField(
        label='プレゼントの種類',
        choices=PRESENT_CHOICES,
        required=False
    )
    
    range_of_amounts = forms.ChoiceField(
        label='金額の範囲',
        choices=AMOUNT_RANGE_CHOICES,
        required=False
    )
    
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
            'relationships': '関係性',
            'purpose': '目的',
            'present': 'プレゼント',
            'present_type': 'プレゼントの種類',
            'range_of_amounts': '金額の範囲',
            'amount_of_money': '金額',
            'photo': '写真',
            'memories': '思い出',
            'self_assessment': '自己評価',
            'improvements': '改善点',
            # その他のフィールドのラベルもここに追加してください
        }
       
