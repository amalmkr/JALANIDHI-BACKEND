from rest_framework import serializers
from .models import Bill,Payment
from .service import bill_calculator


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields='__all__'
        read_only_fields=['amount']

    def validate(self,data):
        connection=data['connection']
        meter_reading=data['meter_reading']

        if meter_reading.connection!=connection:
            raise serializers.ValidationError(
                "Meter reading does not belong to this connection"
            )
        return data

    def create(self,validated_data):
        meter_reading=validated_data['meter_reading']
        water_used=meter_reading.water_used
        amount=bill_calculator(water_used)
        validated_data['amount']=amount
        return Bill.objects.create(**validated_data)



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

    def validate(self,data):
        bill=data['bill']
        amount=data['amount']

        if amount!=bill.amount:
            raise serializers.ValidationError(
                "payment amount didnt match with bill amount"
            )
        return data
            

    def create(self,validated_data):
        payment=Payment.objects.create(**validated_data)

        if payment.payment_status=="SUCCESS":
            payment.bill.is_paid=True
            payment.bill.save()

        return payment
            



