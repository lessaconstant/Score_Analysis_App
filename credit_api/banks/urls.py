from django.urls import path
from .views import BankListCreateView, BankDetailView

urlpatterns = [
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),
]
