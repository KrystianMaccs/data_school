from django.db import models
from apps.common.models import TimeStampedUUIDModel

class PayStackCustomerInfo(TimeStampedUUIDModel):
    full_name= models.CharField(max_length  = 150)
    email= models.EmailField()
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 150)

"""class StripeCustomerInfo(TimeStampedUUIDModel):
    pass"""
