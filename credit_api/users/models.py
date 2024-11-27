from django.contrib.auth.models import AbstractUser
from django.utils import timezone 
from django.db import models
from banks.models import Bank

class CustomUser(AbstractUser):
    # Idade do cliente
    age = models.PositiveIntegerField()

    # Sexo do cliente (F ou M)
    gender = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])

    # Data de criação do usuário
    account_creation_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    # Bancos cadastrados
    banks = models.ManyToManyField(Bank, related_name='users')

    # Número de dependentes do cliente
    dependents = models.PositiveIntegerField(default=0)

    # Nível de escolaridade do cliente
    education_level = models.CharField(max_length=50)

    # Faixa salarial do cliente
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)

    # Tipo de cartão do cliente
    card_type = models.CharField(max_length=50)

    # Quantidade de produtos comprados nos últimos 12 meses
    products_purchased_12m = models.PositiveIntegerField()

    # Quantidade de interações/transações nos últimos 12 meses
    interactions_12m = models.PositiveIntegerField()

    # Quantidade de meses que o cliente ficou inativo nos últimos 12 meses
    inactive_months_12m = models.PositiveIntegerField()

    # Limite de crédito do cliente
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)

    # Valor das transações dos últimos 12 meses
    transaction_value_12m = models.DecimalField(max_digits=10, decimal_places=2)

    # Quantidade de transações dos últimos 12 meses
    transaction_count_12m = models.PositiveIntegerField()

    # Score de crédito do cliente
    credit_score = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)

    # Define se o usuário é um gerente
    is_manager = models.BooleanField(default=False)  

    def __str__(self):
        return self.username
