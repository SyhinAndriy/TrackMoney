# Generated by Django 4.1.7 on 2023-05-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_delete_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=30)),
                (
                    "category_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.categorytype",
                    ),
                ),
            ],
        ),
    ]
