from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)  # Nome do banco
    code = models.CharField(max_length=10, unique=True)  # Código único do banco
    country = models.CharField(max_length=50)  # País onde o banco está localizado

    def __str__(self):
        return f'{self.name} ({self.code})'

