# Generated by Django 5.0 on 2024-01-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, help_text="Enter the investment amount", max_digits=19
            ),
        ),
    ]
