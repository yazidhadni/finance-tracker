from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Investment


class InvestmentForm(forms.ModelForm):
    edit_investment = forms.BooleanField(widget=forms.HiddenInput, initial=True)

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
            "date_invested": DatePickerInput(),
        }

    # validators
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount is not None and amount < 0:
            raise forms.ValidationError("Amount must be a non-negative value.")
        return amount


class DeleteInvestmentForm(forms.Form):
    delete_investment = forms.BooleanField(widget=forms.HiddenInput, initial=True)
