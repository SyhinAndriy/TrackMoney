from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def index_view(request):
    account = Account.objects.filter(user=request.user).order_by('-priority').first()
    if not account:
        account = Account.objects.create(name='My Wallet', user=request.user, priority=True)
        account.save()
    context = {
        "account": account
    }
    return render(request, 'app/index.html', context)


def cards_view(request):
    accounts = Account.objects.filter(user=request.user)
    context = {
        "accounts": accounts
    }
    return render(request, 'app/all_cards.html', context)


def update_card(request):
    if request.user.is_authenticated:
        new_balance = request.POST.get("card_balance")
        account_id = request.POST.get("id")
        account = Account.objects.get(pk=account_id)
        account.balance = new_balance
        account.save()
        return JsonResponse({"data": new_balance, "status": "Successfully"})
    return JsonResponse({"status": "Error. Cannot update card balance"})
