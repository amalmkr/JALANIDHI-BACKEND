from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import BillSerializer,PaymentSerializer
from .models import Payment,Bill


class BillListCreateView(APIView):
    def get(self,request):
        bill=Bill.objects.all()
        serializer=BillSerializer(bill,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Billdetails(APIView):
    def get(self,request,id):
        bill=get_object_or_404(Bill,id=id)
        serializer=BillSerializer(bill)
        return Response(serializer.data)

    def put(self,request,id):
        bill=get_object_or_404(Bill,id=id)

        serializer=BillSerializer(bill,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request,id):
        bill=get_object_or_404(Bill,id=id)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,id):
        bill=get_object_or_404(Bill,id=id)

        serializer=BillSerializer(bill,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        



    

class PaymentListCreateView(APIView):
    def get(self,request):
        payment=Payment.objects.all()
        serializer=PaymentSerializer(payment,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Paymentdetails(APIView):
    def get(self,request,id):
        payment=get_object_or_404(Payment,id=id)
        serializer=PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id):
        payment=get_object_or_404(Payment,id=id)
        serializer=PaymentSerializer(payment,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        payment=get_object_or_404(Payment,id=id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,id):
        payment=get_object_or_404(Payment,id=id)
        serializer=PaymentSerializer(payment,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
   