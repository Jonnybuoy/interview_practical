from django.contrib import admin

from .models import Account, Transaction, Deposit, Withdrawal

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
