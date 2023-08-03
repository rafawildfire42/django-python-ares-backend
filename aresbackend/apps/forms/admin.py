from django.contrib import admin
from .models import BudgetForm

class BudgetFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cpf', 'phone', 'email', 'service', 'return_way')
    list_filter = ('service', 'return_way')
    search_fields = ('first_name', 'last_name', 'cpf', 'phone', 'email')

admin.site.register(BudgetForm, BudgetFormAdmin)