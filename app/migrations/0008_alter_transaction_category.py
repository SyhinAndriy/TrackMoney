# Generated by Django 4.1.7 on 2023-05-26 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_categorytype_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.category"
            ),
        ),
    ]