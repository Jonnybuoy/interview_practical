from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Account, Transaction, Deposit, Withdrawal


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = '__all__'


class DepositsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deposit
        fields = '__all__'


class WithdrawalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdrawal
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
