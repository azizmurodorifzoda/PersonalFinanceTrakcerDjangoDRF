from django import forms
from .models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'description']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']