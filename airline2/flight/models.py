from django.db import models

# Create your models here.
class Flight(models.Model):
    origin =   models.CharField(max_length=3)
    destination = models.CharField(max_length=64)

    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0
