from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bank
from .serializers import BankSerializer

class BankListCreateView(APIView):
    def get(self, request):
        banks = Bank.objects.all()  
        serializer = BankSerializer(banks, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = BankSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankDetailView(APIView):
    def get_object(self, pk):
        try:
            return Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            return None

    def get(self, request, pk):
        bank = self.get_object(pk)
        if bank is not None:
            serializer = BankSerializer(bank)
            return Response(serializer.data)
        return Response({'error': 'Banco não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        bank = self.get_object(pk)
        if bank is not None:
            serializer = BankSerializer(bank, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Banco não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        bank = self.get_object(pk)
        if bank is not None:
            bank.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Banco não encontrado'}, status=status.HTTP_404_NOT_FOUND)
