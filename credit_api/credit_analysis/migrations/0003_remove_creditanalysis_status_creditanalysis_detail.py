# Generated by Django 5.1 on 2024-11-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_analysis', '0002_creditanalysis_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditanalysis',
            name='status',
        ),
        migrations.AddField(
            model_name='creditanalysis',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]