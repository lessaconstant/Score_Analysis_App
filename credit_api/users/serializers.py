from rest_framework import serializers
from .models import CustomUser
from banks.models import Bank
from banks.serializers import BankSerializer 

class CustomUserSerializer(serializers.ModelSerializer):
    banks = BankSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'age', 'gender', 'dependents', 'education_level',
            'annual_income', 'card_type', 'products_purchased_12m', 'interactions_12m',
            'inactive_months_12m', 'credit_limit', 'transaction_value_12m',
            'transaction_count_12m', 'credit_score', 'banks'
        ]
