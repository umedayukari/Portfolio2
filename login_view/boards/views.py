from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from . import forms
from django.contrib import messages
from .models import Themes
from .models import AnniversaryRecords, Opponent
from .forms import AnniversaryRecordForm, OpponentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import PRESENT_CHOICES, AMOUNT_RANGE_CHOICES


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

def delete_anniversary_record(request, id):
    anniversary_record = get_object_or_404(AnniversaryRecords, id=id)
    # 記念日の所有者が現在のユーザーであることを確認
    if anniversary_record.opponent.user != request.user:
        raise Http404
    if request.method == 'POST':  # 安全な削除のためPOSTリクエストを確認
        anniversary_record.delete()
        messages.success(request, '記念日の記録が削除されました。')
        return redirect('boards:anniversary_records')
    else:
        # GETリクエストの場合は削除確認ページを表示するか、または直接リダイレクト
        return redirect('boards:anniversary_records')

    
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

def edit_opponent(request, id):
    opponent = get_object_or_404(Opponent, id=id, user=request.user)
    if request.method == 'POST':
        form = OpponentForm(request.POST, instance=opponent)
        if form.is_valid():
            form.save()
            messages.success(request, 'お相手の情報を更新しました')
            return redirect('boards:opponent_list')
    else:
        form = OpponentForm(instance=opponent)
    
    return render(request, 'boards/edit_opponent_record.html', {'form': form})

def delete_opponent(request, id):
    opponent = get_object_or_404(Opponent, id=id, user=request.user)
    if request.method == 'POST':
        opponent.delete()
        messages.success(request, 'お相手を削除しました')
        next_url = request.POST.get('next', 'boards:opponent_list')
        return redirect(next_url)
    
    # 通常は直接削除リンクにGETリクエストを許可しないため、ここは適宜調整
    return redirect('boards:opponent_list')



def search(request):
    query = request.GET.get('query', '')
    present_type = request.GET.get('present_type', '')
    amount_range = request.GET.get('amount_range', '')
    
    results = AnniversaryRecords.objects.all()

    if query:
        results = results.filter(
            Q(present_type__icontains=query) |
            Q(purpose__icontains=query) |
            Q(opponent__name__icontains=query)
        )
    
    if present_type:
        results = results.filter(present_type=present_type)
        
    if amount_range:
        results = results.filter(amount_range=amount_range)

    return render(request, 'boards/search_results.html', {
        'results': results,
        'present_choices': PRESENT_CHOICES,
        'amount_range_choices': AMOUNT_RANGE_CHOICES
    })