from django.db import models
from connections.models import Connection

class MeterReading(models.Model):
    connection=models.ForeignKey(
        Connection,
        on_delete=models.CASCADE,
        related_name="meter_readings"
    )

    previous_reading=models.DecimalField(decimal_places=2,max_digits=10)
    current_reading=models.DecimalField(decimal_places=2,max_digits=10)
    water_used=models.DecimalField(default=0,decimal_places=2,max_digits=10)

    reading_date=models.DateField()

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.connection} - {self.reading_date}"

    def save(self,*args,**kwargs):
        self.water_used=self.current_reading - self.previous_reading
        super().save(*args,**kwargs)
        
