from django.db import models
from connections.models import Connection
from meter_readings.models import MeterReading


class Bill(models.Model):
    connection=models.ForeignKey(
        Connection,
        on_delete=models.CASCADE,
        related_name="bills"
    )

    meter_reading=models.OneToOneField(
        MeterReading,
        on_delete=models.CASCADE,
        related_name='bill'
    )

    bill_number=models.CharField(max_length=50,unique=True)
    bill_month=models.DateField()
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    is_paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill_number}-{self.connection}"


class Payment(models.Model):
    bill =models.OneToOneField(
        Bill,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    transaction_id=models.CharField(unique=True,max_length=100)
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    payment_status=models.CharField(max_length=20,default="SUCCESS")
    payment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id}-{self.payment_status}"