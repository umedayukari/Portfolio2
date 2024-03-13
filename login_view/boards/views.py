from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from . import forms
from django.contrib import messages
from .models import Themes
from .models import AnniversaryRecords, Opponent
from .forms import AnniversaryRecordForm, OpponentForm


def register_anniversary(request): 
    if request.method == 'POST':
        form = AnniversaryRecordForm(request.POST, request.FILES)
        if form.is_valid():
            anniversary_record = form.save(commit=False)
            anniversary_record.user = request.user  # 必要であればユーザーを関連付けます
            anniversary_record.save()
            messages.success(request, '記念日の登録が完了しました')
            return redirect('boards:anniversary_list')
    else:
        form = AnniversaryRecordForm()

    return render(
        request, 
        'boards/register_anniversary.html',
        context={'register_anniversary_form': form}
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
    opponents = Opponent.objects.filter(user=request.user)
    anniversary_records = AnniversaryRecords.objects.filter(opponent__in=opponents).order_by('-date_created')
    form = AnniversaryRecordForm()
    return render(
        request, 'boards/anniversary_list.html', {
            'anniversary_records': anniversary_records,
            'form': form
    })

def edit_anniversary_record(request, id):
    # opponent__user=request.user を使用して、ユーザーに紐づく記念日レコードをフィルタリング
    anniversary_record = get_object_or_404(AnniversaryRecords, id=id, opponent__user=request.user)
    if request.method == 'POST':
        form = AnniversaryRecordForm(request.POST, request.FILES, instance=anniversary_record)
        if form.is_valid():
            form.save()
            messages.success(request, '記念日を更新しました')
            return redirect('boards:anniversary_list')
    else:
        form = AnniversaryRecordForm(instance=anniversary_record)

    return render(
        request, 
        'boards/edit_anniversary_record.html', 
        context={'form': form, 'id': id}
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
            return redirect('boards:opponent_list')  
    else:
        form = OpponentForm()
    return render(request, 'boards/register_opponent.html', {'form': form})

def opponent_list(request):
    opponents = Opponent.objects.filter(user=request.user)# ログインユーザーに関連するお相手の一覧
    return render(request, 'boards/opponent_list.html', {'opponents': opponents})


def search(request):
    # 検索機能に関する処理をここに実装します。
    pass

