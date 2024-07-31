from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'transaction_type', 'date']
    list_filter = ['transaction_type', 'date']
    search_fields = ['user__username', 'category__name', 'description']
