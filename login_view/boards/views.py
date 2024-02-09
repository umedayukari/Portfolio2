from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import Themes
from .models import AnniversaryRecords
from .forms import OpponentForm
from .models import Opponent

# Create your views here.
def register_anniversary(request): 
    register_anniversary_form = forms.CreateThemeForm(request.POST or None)  
    
    if  register_anniversary_form.is_valid():
        register_anniversary_form.instance.user = request.user
        register_anniversary_form.save()
        messages.success(request, '作成完了しました')
        return redirect('boards:anniversary_records')  
    
    return render(
        request, 
        'boards/register_anniversary.html',
        context={  
            'register_anniversary_form':register_anniversary_form}
    )
def anniversary_records(request):
    # このビューではお相手の登録フォームを表示する
    opponent_form = OpponentForm()
    return render(
        request, 
        'boards/anniversary_list.html', 
        context={'opponent_form': opponent_form}
    )

    
def list_anniversary_records(request):
    create_anniversary_record_form = OpponentForm()
    return render(
        request, 'boards/anniversary_list.html', {
            'create_anniversary_record_form': create_anniversary_record_form}
    )
    
def register_opponent(request):
    # お相手の登録に関する処理をここに実装します。
    if request.method == 'POST':
        form = OpponentForm(request.POST)
        if form.is_valid():
            opponent = form.save(commit=False)
            opponent.user = request.user  # ログイン中のユーザーを設定
            opponent.save()
            messages.success(request, 'お相手の登録が完了しました')
            return redirect('account:home')  
    else:
        form = OpponentForm()
    return render(request, 'boards/register_opponent.html', {'form': form})

def opponent_list(request):
    opponents = Opponent.objects.filter(user=request.user)  # ログインユーザーに関連するお相手の一覧
    return render(request, 'boards/opponent_list.html', {'opponents': opponents})


def search(request):
    # 検索機能に関する処理をここに実装します。
    pass
