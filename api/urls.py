from django.urls import path
from .views import  *
from rest_framework.routers import DefaultRouter  

router = DefaultRouter()  
router.register(r'transactions', TransactionListView)  

urlpatterns = [
    # path('report/', report_view, name='report_view'),
    

    path('categories', CategoryListView.as_view()),
    path('categories-create/', CategoryCreateView.as_view()),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view()),
    path('categories-delate/<int:pk>', CategoryDelateView.as_view()),



    path('transactions/', TransactionListView.as_view()),
    path('transactions-create/', TransactionCreateView.as_view()),
    path('transactions-update/<int:pk>', TransactionUpdateView.as_view()),
    path('transactions-delate/<int:pk>', TransactionDelateView.as_view()),


    # path('api/register/', RegisterView.as_view(),),

]
