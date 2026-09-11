from django.db import models
from users.models import User

class Connection(models.Model):
    STATUS_CHOICES=[

        ("PENDING","pending"),
        ("APPROVED","approved"),
        ("REJECTED","rejected"),
        ("ACTIVE","active"),
        ("DISCONNECTED","disconnected")
    ]

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    consumer_number=models.CharField(
        max_length=20,
        unique=True,
        null=True,blank=True
    )

    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="connection"
    )

    house_number=models.CharField(max_length=50)
    house_name=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    address=models.TextField()
    pin=models.CharField(max_length=6)

    id_proof=models.FileField(upload_to='documents/id_proof/')
    address_proof=models.FileField(upload_to='documents/address_proof/')
    ownership_proof=models.FileField(upload_to='documents/ownership_proof/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}-{self.house_number}"


class ConsumerSequence(models.Model):
    next_number=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Next Consumer Number : {self.next_number}"