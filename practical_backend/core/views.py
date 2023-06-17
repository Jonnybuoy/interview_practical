from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Account, Transaction, Deposit, Withdrawal
from .serializers import AccountSerializer, TransactionSerializer, DepositsSerializer, WithdrawalsSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/accounts'},
        {'POST': 'api/users/token'}
    ]
    return Response(routes)


@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serialize = AccountSerializer(accounts, many=True)
    return Response(serialize.data)


@api_view(['GET', 'POST'])
def deposits_view(request):
    if request.method == 'GET':
        deposits = Deposit.objects.all()
        serializer = DepositsSerializer(deposits, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deposit_amount = serializer.validated_data['deposit_amount']
        serialized_account = serializer.validated_data['account']
        
        account = Account.objects.filter(user__username=str(serialized_account)).first()
        account.balance += deposit_amount
        account.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def withdrawals_view(request):
    if request.method == 'GET':
        withdrawals = Withdrawal.objects.all()
        serializer = WithdrawalsSerializer(withdrawals, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WithdrawalsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        withdrawal_amount = serializer.validated_data['withdrawal_amount']
        serialized_account = serializer.validated_data['account']
        
        account = Account.objects.filter(user__username=str(serialized_account)).first()
        account.balance -= withdrawal_amount
        account.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def transaction_view(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        serialized_receiver_account = serializer.validated_data['receiver']
        serialized_sender_account = serializer.validated_data['sender']
        
        receiver_account = Account.objects.filter(user__username=str(serialized_receiver_account)).first()
        sender_account = Account.objects.filter(user__username=str(serialized_sender_account)).first()
        if not receiver_account:
            return Response({'error': 'Receiver account not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if sender_account.balance < amount:
            return Response({'error': 'You have insufficient balance in your account.'}, status=status.HTTP_400_BAD_REQUEST)
        
        sender_account.balance -= amount
        receiver_account.balance += amount
        with transaction.atomic():
            sender_account.save()
            receiver_account.save()
            Transaction.objects.create(sender=sender_account, receiver=receiver_account, amount=amount)
        
        return Response({'message': 'Transfer successful.'}, status=status.HTTP_200_OK)
            
            
    
