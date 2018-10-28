from django.db import models
from .airline import Airline


class Flight(models.Model):
    flight_code = models.CharField(max_length=100,primary_key=True)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    passenger_capacity = models.IntegerField()

    def __str__(self):
        return self.flight_code
