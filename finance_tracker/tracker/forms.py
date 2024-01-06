from django import forms

from .models import Investment


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = [
            "name",
            "amount",
            "currency",
            "date_invested",
            "description",
            "is_current",
            "investment_type",
            "source",
        ]
