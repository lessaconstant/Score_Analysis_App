from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import CreditAnalysis
from .ml_models import predict_credit_score
from datetime import datetime
from django.utils import timezone

class CreditAnalysisView(APIView):

    # Listar todas as solicitações (Histórico Completo)
    def get(self, request):
        # Filtrando apenas as análises com status 'P' (Pendente)
        pending_analyses = CreditAnalysis.objects.filter(status='P')
        
        # Preparando a resposta com os dados necessários
        data = [
            {
                'user_id': analysis.user.id,
                'user_name': analysis.user.username,
                'credit_score': analysis.credit_score,
                'status': analysis.status,
                'analysis_date': analysis.analysis_date,
                'detail':analysis.detail
            }
            for analysis in pending_analyses
        ]
        
        # Retornando os dados com status HTTP 200 OK
        return Response(data, status=status.HTTP_200_OK)
    # Criar nova análise de crédito (quando o cliente faz a solicitação)
    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        # Calcular meses de relacionamento
        hoje = timezone.now()
        meses_de_relacionamento = (hoje.year - user.account_creation_date.year) * 12 + hoje.month - user.account_creation_date.month

        # Dados do usuário para prever o score de crédito
        user_data = {
            'idade': user.age,
            'sexo': 1 if user.gender == 'M' else 0, 
            'dependentes': user.dependents,
            'escolaridade': user.education_level,
            'salario_anual': user.annual_income,
            'tipo_cartao': user.card_type,
            'qtd_produtos': user.products_purchased_12m,
            'iteracoes_12m': user.interactions_12m,
            'meses_inativos_12m': user.inactive_months_12m,
            'meses_de_relacionamento': meses_de_relacionamento,
            'limite_credito': user.credit_limit,
            'valor_transacoes_12m': user.transaction_value_12m,
            'qtd_transacoes_12m': user.transaction_count_12m
        }

        # Previsão do score de crédito
        credit_score = predict_credit_score(user_data)

        # Atualiza o credit_score do usuário
        user.credit_score = credit_score
        user.save()

        # Detalhe opcional da solicitação
        detail = request.data.get('detail', None)

        # Criação da análise de crédito com status "Pendente"
        CreditAnalysis.objects.create(
            user=user,
            credit_score=credit_score,
            status='P',  # "P" significa Pendente
            detail=detail
        )

        return Response({'credit_score': credit_score}, status=status.HTTP_200_OK)
    
    
    # Alterar o status da análise de crédito (Aprovar ou Rejeitar)
    def patch(self, request, user_id):
        # Verificar se o gerente enviou o status
        status_choice = request.data.get('status')
        if status_choice not in ['A', 'R']:
            return Response({'error': 'Status inválido. Use "A" para Aprovar ou "R" para Rejeitar.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            credit_analysis = CreditAnalysis.objects.get(user=user)
        except CreditAnalysis.DoesNotExist:
            return Response({'error': 'Análise de crédito não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Atualizando o status da análise de crédito
        credit_analysis.status = status_choice
        credit_analysis.save()

        return Response({
            'message': 'Status atualizado com sucesso',
            'new_status': credit_analysis.status
        }, status=status.HTTP_200_OK)
