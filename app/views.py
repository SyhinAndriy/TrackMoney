from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def index_view(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    context = {
        "card_balance": account.amount
    }
    return render(request, 'app/index.html', context)


def update_card(request):
    if request.user.is_authenticated:
        data = request.POST.get("card_balance")
        account = Account.objects.get(user=request.user)
        account.amount = data
        account.save()
        return JsonResponse({"data": data, "status": "Successfully"})
    return JsonResponse({"status": "Error. Cannot update card balance"})
