from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=10, unique=True)
    identity=models.CharField(max_length=50)

# to show name as main heading
    def __str__(self):
        return self.name