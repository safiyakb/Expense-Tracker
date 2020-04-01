from django.contrib import admin
from expense.models import Expense, Income, Wallet
# Register your models here.

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Wallet)
