from django.shortcuts import render

from .forms import PayStackCustomerInfoForm

def initiate_payment(request: HttpRequest):
    if request.method == "POST":
        payment_form = forms.Payment(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
    