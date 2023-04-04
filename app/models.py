
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('TRANSFER', 'Transfer'),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    category = models.CharField(max_length=266)

    def __str__(self):
        return self.category

    class Meta:

        ordering: ["-date"]
