# Generated by Django 4.1.7 on 2023-04-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
