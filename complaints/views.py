from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintListCreateView(APIView):


    def get(self,request):
        complaint=Complaint.objects.all()
        serializer=ComplaintSerializer(complaint,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ComplaintSerializer(data=request.data)

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

class ComplaintDetailsView(APIView):

    

    def get(self,request,id):
        complaint=get_object_or_404(Complaint,id=id)
        serializer=ComplaintSerializer(complaint)
        return Response(serializer.data)

    def put(self,request,id):
        complaint=get_object_or_404(Complaint,id=id)
        serializer=ComplaintSerializer(complaint,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self,request,id):
        complaint=get_object_or_404(Complaint,id=id)
        complaint.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # complaints/views.py — inside ComplaintDetailsView
    def patch(self, request, id):
        complaint = get_object_or_404(Complaint, id=id)
        serializer = ComplaintSerializer(
            complaint,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

