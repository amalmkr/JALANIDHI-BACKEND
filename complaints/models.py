from django.db import models
from connections.models import Connection

class Complaint(models.Model):
    connection=models.ForeignKey(
        Connection,
        on_delete=models.CASCADE,
        related_name='complaints',
        null=True,
        blank=True
    )

    mobile_number=models.CharField(max_length=10)
    complaint_type=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    location=models.CharField(max_length=255)
    complaint_details=models.TextField()
    status=models.CharField(max_length=20,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complaint_type}-{self.mobile_number}"

