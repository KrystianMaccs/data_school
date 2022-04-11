from django.db import models
from apps.common.models import TimeStampedUUIDModel

class PayStackCustomerInfo(TimeStampedUUIDModel):
    #full_name= models.OneToOneField(Student, on_delete=models.CASCADE, max_length  = 150)
    amount = models.PositiveIntegerField()
    email= models.EmailField()
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = PayStackCustomerInfo.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self):
        return self.amount


"""class StripeCustomerInfo(TimeStampedUUIDModel):
    pass"""
