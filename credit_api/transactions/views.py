from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, pk):
        transaction = self.get_object(pk)
        if transaction is not None:
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        return Response({'error': 'Transação não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        transaction = self.get_object(pk)
        if transaction is not None:
            serializer = TransactionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Transação não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        if transaction is not None:
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Transação não encontrada'}, status=status.HTTP_404_NOT_FOUND)
