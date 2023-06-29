import json
import pytz
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .models import *
from django.db.models import Sum


# Create your views here.

def index_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    account = Account.objects.filter(user=request.user).order_by('-priority').first()
    if not account:
        account = Account.objects.create(name='My Wallet', user=request.user, priority=True)
        account.save()

    expense_categories = Category.objects.filter(category_type__name='Expense')
    expense_categories_names = json.dumps([category.category_name for category in expense_categories])

    income_categories = Category.objects.filter(category_type__name='Income')
    income_categories_names = json.dumps([category.category_name for category in income_categories])

    # get last transactions
    transactions = Transaction.objects.filter(account__user=request.user).order_by('-date')

    context = {
        "account": account,
        "transactions": transactions,
        'expense_categories': expense_categories_names,
        'income_categories': income_categories_names,

    }
    return render(request, 'app/index.html', context)


def cards_view(request):
    if request.user.is_authenticated:

        accounts = Account.objects.filter(user=request.user)
        context = {
            "accounts": accounts
        }
        return render(request, 'app/all_cards.html', context)
    else:
        return redirect('login')


def update_card(request):
    if request.user.is_authenticated:
        new_balance = request.POST.get("card_balance")
        account_id = request.POST.get("id")
        account = Account.objects.get(pk=account_id)
        account.balance = new_balance
        account.save()
        return JsonResponse({"data": new_balance, "status": "Successfully"})
    return JsonResponse({"status": "Error. Cannot update card balance"})


def add_transaction(request):
    # get data from form
    # transaction_slug = request.POST.get('type')
    amount = float(request.POST.get('amount'))
    category = request.POST.get('category')
    account_id = request.POST.get("id")

    category = Category.objects.get(category_name=category)
    category_type = category.category_type.name
    # create new transaction
    if category_type == "Expense":

        amount = -amount
    elif category_type == 'Income':
        pass
    else:
        return JsonResponse({
            "status": "Error",
        })
    account = Account.objects.get(pk=account_id)
    new_transaction = Transaction.objects.create(amount=amount, account=account,
                                                 category=category)
    new_transaction.save()

    # update account balance
    new_balance = float(account.balance) + amount
    account.balance = new_balance
    account.save()

    return JsonResponse({
        "status": "Successfully",
        "data": new_balance
    })


def add_card(request):
    card_name = request.POST.get('name')
    balance = request.POST.get('card_balance')
    print(card_name, balance)
    new_card = Account.objects.create(name=card_name, user=request.user, balance=balance)
    new_card.save()
    return JsonResponse({
        "status": "Successfully",
    })


def select_card(request, card_id):
    old_card = Account.objects.get(priority=True)
    old_card.priority = False
    old_card.save()

    new_card = Account.objects.get(id=card_id)
    new_card.priority = True
    new_card.save()
    return redirect('index')


def view_statistic(request):
    context = {}
    return render(request, 'app/inc/statistic.html', context)


def get_filtered_data(request):
    current_timezone = pytz.timezone("Europe/Kiev")
    # Отримання параметрів фільтрації з GET-запиту
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    start_date = start_date.astimezone(current_timezone)

    end_date = end_date.astimezone(current_timezone)

    print(start_date)

    user = request.user  # користувач
    total_expenses = Transaction.objects.filter(
        category__category_type__name='Expense',  # Фільтруємо тільки витрати
        date__range=(start_date, end_date),  # Фільтруємо за проміжком часу
        account__user=user  # Фільтруємо за  користувачем
    ).values('category__category_name').annotate(total_amount=Sum('amount'))

    category_names = [expense['category__category_name'] for expense in total_expenses]
    total_amounts = [expense['total_amount'] for expense in total_expenses]

    print(category_names)
    print(total_amounts)

    # Приклад даних, які повертаються
    data = {
        'labels': category_names,
        'expensesData': total_amounts,
        'sum': sum(total_amounts)
        # 'incomeData': [500, 700, 300, 450, 600]
    }

    return JsonResponse(data)
