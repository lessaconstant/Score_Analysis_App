from django.urls import path
from .views import CreditAnalysisView

urlpatterns = [
    path('credit-analysis/', CreditAnalysisView.as_view(), name='credit_analysis_list'),
    path('credit-analysis/pending/', CreditAnalysisView.as_view(), name='credit_analysis_pending'),  # Rota para as pendentes
    path('credit-analysis/<int:user_id>/', CreditAnalysisView.as_view(), name='create_credit_analysis'),
    path('credit-analysis/<int:user_id>/update/', CreditAnalysisView.as_view(), name='update_credit_analysis'),
]
