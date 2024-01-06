from django.conf import settings
from django.db import models


class Investment(models.Model):
    CURRENCY_CHOICES = [
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
        ("MAD", "Moroccan Dirham"),
        ("BTC", "Bitcoin"),
        ("ETH", "Ethereum"),
        ("DOT", "Polkadot"),
        ("SOL", "Solana"),
        ("ATOM", "Cosmos"),
        ("MANA", "Decentraland"),
        ("FLOW", "Flow"),
        # Add more currency choices as needed
    ]
    INVESTMENT_CHOICES = [
        ("Stock", "Stock"),
        ("PE", "Private Equity"),
        ("ETF", "ETF"),
        ("Real Estate", "Real Estate"),
        ("Life Insurance", "Life Insurance"),
        ("Crypto", "Crypto"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, help_text="Enter the name of the investment")
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, help_text="Enter the investment amount"
    )
    currency = models.CharField(
        max_length=5,
        choices=CURRENCY_CHOICES,
        default="EUR",
        help_text="Select the currency",
    )
    date_invested = models.DateField(help_text="Enter the date of the investment")
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Provide a description of the investment (optional)",
    )
    is_current = models.BooleanField(
        default=True, help_text="Is this investment still active?"
    )
    investment_type = models.CharField(
        max_length=30,
        choices=INVESTMENT_CHOICES,
        help_text="Select the type of investment",
    )
    source = models.CharField(
        max_length=30,
        help_text="Enter the source of the investment (e.g: 'Boursorama')",
    )

    def __str__(self):
        return self.name
