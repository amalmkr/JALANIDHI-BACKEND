from rest_framework import serializers
from .models import Complaint
from .services import generate_complaint_reference
from connections.models import Connection


class ComplaintSerializer(serializers.ModelSerializer):

    consumer_number = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = Complaint
        fields = "__all__"

    def create(self, validated_data):

        consumer_number = validated_data.pop("consumer_number", None)

        if consumer_number:
            try:
                connection = Connection.objects.get(
                    consumer_number=consumer_number
                )
            except Connection.DoesNotExist:
                raise serializers.ValidationError({
                    "consumer_number": "Invalid consumer number."
                })

            validated_data["connection"] = connection

        complaint_reference = generate_complaint_reference()
        validated_data["complaint_reference"] = complaint_reference

        return Complaint.objects.create(**validated_data)