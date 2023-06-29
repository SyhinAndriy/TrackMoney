from django.contrib import admin

from app.models import *


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'description', 'account', 'category')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'balance',)


admin.site.register(Category)
admin.site.register(CategoryType)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
