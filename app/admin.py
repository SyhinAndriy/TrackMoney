from django.contrib import admin

from app.models import *


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'date', 'description', 'account', 'category')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount',)


admin.site.register(Category)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
