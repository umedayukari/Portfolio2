from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import Themes
from .models import AnniversaryRecords
from .forms import OpponentForm

# Create your views here.
def create_anniversary_record(request): 
    create_anniversary_record_form = forms.CreateThemeForm(request.POST or None)  
    if create_anniversary_record_form.is_valid():
        create_anniversary_record_form.instance.user = request.user
        create_anniversary_record_form.save()
        messages.success(request, '記念日の記録が新しく作成されました')
        return redirect('boards:list_anniversary_records')  # リダイレクト先の変更が必要な場合はこちらも変更
    
    return render(
        request, 'boards/anniversary_record.html', context={  # テンプレート名の変更
            'create_anniversary_record_form': create_anniversary_record_form,  # 変数名の変更
        }
    )
    
def list_anniversary_records(request):
    gift_records = AnniversaryRecords.objects.all()
    return render(
        request, 'boards/anniversary_record.html', {
            'gift_records': gift_records
        }
    )
    
def register_partner(request):
    # お相手の登録に関する処理をここに実装します。
    if request.method == 'POST':
        form = OpponentForm(request.POST)
        if form.is_valid():
            opponent = form.save(commit=False)
            opponent.user = request.user  # ログイン中のユーザーを設定
            opponent.save()
            messages.success(request, 'お相手の登録が完了しました')
            return redirect('account:home')  # 適切なリダイレクト先に変更してください
    else:
        form = OpponentForm()
    return render(request, 'boards/register_partner.html', {'form': form})

def register_present(request):
    # プレゼントの登録に関する処理をここに実装します。
    pass

def search(request):
    # 検索機能に関する処理をここに実装します。
    pass
