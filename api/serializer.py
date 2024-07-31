from rest_framework import serializers
from .models import Category, Transaction
from django.contrib.auth.models import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["user", "category", "amount", "transaction_type", "date", "description"]

class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["user", "category", "amount", "transaction_type", "date", "description"]


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user
    

# class CustomRegisterSerializer(RegisterSerializer):
    # first_name = serializers.CharField(required=True)
    # last_name = serializers.CharField(required=True)

    # def get_cleaned_data(self):
    #     data = super().get_cleaned_data()
    #     data['first_name'] = self.validated_data.get('first_name', '')
    #     data['last_name'] = self.validated_data.get('last_name', '')
    #     return data

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])
    #     user.first_name = self.cleaned_data.get('first_name')
    #     user.last_name = self.cleaned_data.get('last_name')
    #     user.save()
    #     return user