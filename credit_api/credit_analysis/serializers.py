from rest_framework import serializers
from .models import CreditAnalysis

class CreditAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditAnalysis
        fields = '__all__'  # Inclui todos os campos do modelo
