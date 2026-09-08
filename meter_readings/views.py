from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import MeterReading
from .serializers import MeterReadingsSerializer

class MeterReadingListCreateView(APIView):
    def get(self,request):
        meter_reading=MeterReading.objects.all()
        serializer=MeterReadingsSerializer(meter_reading,many=True) 
        return Response(serializer.data)

    def post(self,request):
        serializer=MeterReadingsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MeterReadingDetails(APIView):
    def get(self,request,id):
        meter_reading=get_object_or_404(MeterReading,id=id)
        serializer=MeterReadingsSerializer(meter_reading)
        return Response(serializer.data)

    def put(self,request,id):
        meter_reading=get_object_or_404(MeterReading,id=id)
        serializer=MeterReadingsSerializer(meter_reading,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        meter_reading=get_object_or_404(MeterReading,id=id)
        meter_reading.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # meter_readings/views.py — inside MeterReadingDetails
    def patch(self, request, id):
        meter_reading = get_object_or_404(MeterReading, id=id)
        serializer = MeterReadingsSerializer(
            meter_reading,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)