from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializer import *
# from rest_framework import generics, permissions
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import *
# from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TransactionFilter 
from rest_framework import viewsets  
from .models import Transaction, Category  
from .serializer import TransactionSerializer, CategorySerializer  
from .filters import TransactionFilter, CategoryFilter  # Убедитесь, что у вас есть правильные импорты  
from django_filters.rest_framework import DjangoFilterBackend 



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter  


    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CategoryDelateView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]




    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter  

    # def get_queryset(self):
    #     return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]    
    authentication_classes = [JWTAuthentication]



    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDelateView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class Home(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def report_view(request):
#     start_date = request.query_params.get('start_date')
#     end_date = request.query_params.get('end_date')
    
#     if start_date and end_date:
#         start_date = datetime.strptime(start_date, '%Y-%m-%d')
#         end_date = datetime.strptime(end_date, '%Y-%m-%d')
#         transactions = Transaction.objects.filter(user=request.user, date__range=[start_date, end_date])
#     else:
#         transactions = Transaction.objects.filter(user=request.user)
    
#     income = transactions.filter(amount__gt=0).aggregate(total_income=Sum('amount'))['total_income'] or 0
#     expense = transactions.filter(amount__lt=0).aggregate(total_expense=Sum('amount'))['total_expense'] or 0

#     data = {
#         'total_income': income,
#         'total_expense': abs(expense),
#         'net_balance': income + expense,
#         'transactions': TransactionSerializer(transactions, many=True).data
#     }

#     return Response(data)



# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = (AllowAny)
