from .models import PayStackCustomerInfo


class PayStackCustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = "__all__"