from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CategoryType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering: ["-date"]
