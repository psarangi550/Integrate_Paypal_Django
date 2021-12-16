from django.shortcuts import render
from .forms import CoffeeForm
from .models import Coffee

# Create your views here.

def coffe_view(request):
    if request.method=="POST":
        form=CoffeeForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data["amount"]
            return render(request,"CoffeePaymentWithPaypalApp/index.html",{"amount":amount})

    form=CoffeeForm()
    return render(request,"CoffeePaymentWithPaypalApp/index.html",{"form":form})

def thanks_view(request):
    return render(request,"CoffeePaymentWithPaypalApp/checkout.html")
