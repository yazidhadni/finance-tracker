from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import InvestmentForm
from .models import Investment


@login_required
def home(request):
    investments = Investment.objects.all()
    return render(request, "tracker/home.html", {"investments": investments})


@login_required
def add_investment(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            return redirect("tracker:home")
    else:
        form = InvestmentForm()
    return render(request, "tracker/add_investment.html", {"form": form})


@login_required
def view_investment(request, investment_id):
    investment = get_object_or_404(Investment, id=investment_id)
    return render(request, "tracker/view_investment.html", {"investment": investment})
