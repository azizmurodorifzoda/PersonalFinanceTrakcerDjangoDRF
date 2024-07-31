from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from .models import Transaction
from .serializer import TransactionSerializer
from datetime import datetime

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def report_view(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        transactions = Transaction.objects.filter(user=request.user, date__range=[start_date, end_date])
    else:
        transactions = Transaction.objects.filter(user=request.user)
    
    income = transactions.filter(amount__gt=0).aggregate(total_income=Sum('amount'))['total_income'] or 0
    expense = transactions.filter(amount__lt=0).aggregate(total_expense=Sum('amount'))['total_expense'] or 0

    data = {
        'total_income': income,
        'total_expense': abs(expense),
        'net_balance': income + expense,
        'transactions': TransactionSerializer(transactions, many=True).data
    }

    return Response(data)
