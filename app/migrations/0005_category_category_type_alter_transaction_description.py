# Generated by Django 4.1.7 on 2023-05-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_account_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="category_type",
            field=models.CharField(
                choices=[("INCOME", "Income"), ("EXPENSE", "Expense")],
                default="Expense",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
