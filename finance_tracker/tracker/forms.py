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
    
    widgets = {
        'date_invested': forms.DateInput(attrs={'type': 'date'}),
        'amount': forms.TextInput(attrs={'placeholder': 'Enter the investment amount in USD'}),
    }

    # validators
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount is not None and amount < 0:
            raise forms.ValidationError("Amount must be a non-negative value.")
        return amount