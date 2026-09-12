
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintListCreateView(APIView):

    def get(self, request):
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComplaintSerializer(data=request.data)

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

    def get(self, request, id):
        complaint = get_object_or_404(Complaint, id=id)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    def put(self, request, id):
        complaint = get_object_or_404(Complaint, id=id)
        serializer = ComplaintSerializer(
            complaint,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

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

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        complaint = get_object_or_404(Complaint, id=id)
        complaint.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ComplaintStatusView(APIView):

    def patch(self, request, id):

        complaint = get_object_or_404(Complaint,id=id)

        
        new_status = request.data.get("status")

        
        if not new_status:
            return Response(
                {"error": "status is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        allowed_statuses = [
            "PENDING",
            "IN_PROGRESS",
            "RESOLVED",
            "REJECTED"
        ]

        if new_status not in allowed_statuses:
            return Response(
                {"error": "Invalid status."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if complaint.status == "PENDING":

            if new_status not in ["IN_PROGRESS", "REJECTED"]:
                return Response(
                    {"error": "Invalid status transition."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        elif complaint.status == "IN_PROGRESS":

            if new_status != "RESOLVED":
                return Response(
                    {"error": "Invalid status transition."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        elif complaint.status == "RESOLVED":

            return Response(
                {"error": "Resolved complaint cannot be changed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        elif complaint.status == "REJECTED":

            return Response(
                {"error": "Rejected complaint cannot be changed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        complaint.status = new_status
        complaint.save()

        # Return the updated complaint
        serializer = ComplaintSerializer(complaint)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )