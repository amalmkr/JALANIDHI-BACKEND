from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .models import Connection
from .serializers import ConnectionSerializer
from .service import generate_consumer_number



class ConnectionsListCreateView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self,request):
        connections=Connection.objects.all()
        serializer=ConnectionSerializer(
            connections,
            many=True
        )

        return Response(serializer.data)

    def post(self,request):
        serializer=ConnectionSerializer(
            data=request.data
        )

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

class ConnectionDetailView(APIView):

    def get(self,request,id):
        connection=get_object_or_404(Connection,id=id)
        serializer=ConnectionSerializer(connection)
        return Response(serializer.data)

    def put(self,request,id):
        connection=get_object_or_404(Connection,id=id)
        serializer=ConnectionSerializer(connection,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self,request,id):
        connection=get_object_or_404(Connection,id=id)
        connection.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# connections/views.py — inside ConnectionDetailView
    def patch(self, request, id):
        connection = get_object_or_404(Connection, id=id)
        serializer = ConnectionSerializer(
            connection,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConnectionApproveView(APIView): 
    def post(self,request,id):
        connection=get_object_or_404(Connection,id=id)

        if connection.status !="PENDING":
            return Response(
                {"error":"Only pending connection can be approved"},
                status=status.HTTP_400_BAD_REQUEST
            )

        consumer_number=generate_consumer_number()

        connection.consumer_number=consumer_number
        connection.status="APPROVED"
        connection.save()

        serializer=ConnectionSerializer(connection)
        return Response(serializer.data)

    