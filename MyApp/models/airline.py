from django.db import models


class Airline(models.Model):
    airline_code = models.CharField(max_length=128,primary_key=True)
    airline_name = models.CharField(max_length=128)

    def __str__(self):
        return self.airline_name
