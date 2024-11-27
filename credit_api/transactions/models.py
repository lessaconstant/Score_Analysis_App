from django.db import models
from users.models import CustomUser
from banks.models import Bank

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transactions')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da transação
    transaction_date = models.DateTimeField(auto_now_add=True)  # Data da transação
    transaction_type = models.CharField(max_length=50)  # Tipo de transação (compra, saque, transferência, etc.)
    
    def __str__(self):
        return f'{self.transaction_type} - {self.amount} - {self.user.username}'
