from .models import MeterReading
from rest_framework import serializers


class MeterReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MeterReading
        fields="__all__"

    def validate(self,data):
        if data["current_reading"]<data["previous_reading"]:
            raise serializers.ValidationError(
                "Current reading cannot be less than previous reading"
            )

        return data