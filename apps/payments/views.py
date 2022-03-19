from django.shortcuts import render

from .forms import PayStackCustomerInfoForm

def customer_info(request):
    if request.method == "POST":
        customer_form = CustomerInfoForm(request.method)
        if customer_form.is_valid()and customer_form.cleaned_data:
            customer_form.save()
            return render(request, "template_folder/payment.html",
                          {"email":customer_form.email})
        else:
            return HttpResponse("Invalid input try again!!!")
    else:
        customer_form = PayStackCustomerInfoForm()
    return render(request, "template_folder/customer_info.html",
     {"customer_form": customer_form})
