from django.db import models
from apps.common.models import TimeStampedUUIDModel
from apps.membership.models import Student

class PayStackCustomerInfo(TimeStampedUUIDModel):
    full_name= models.OneToOneField(Student, on_delete=models.CASCADE, max_length  = 150)
    email= models.EmailField()
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 150)

    def __str__(self):
        return full_name.title()

"""class StripeCustomerInfo(TimeStampedUUIDModel):
    pass"""
