from django.db import models
from nltk import python_2_unicode_compatible
from .airport import Airport
from .flight import Flight


@python_2_unicode_compatible
class Journey(models.Model):
    flight_code = models.ForeignKey(Flight, on_delete=models.CASCADE)
    origin_airport = models.ForeignKey(Airport, related_name='origin_airport', on_delete=models.CASCADE, default=1100)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE,default=1200)
    Departure_date_time = models.DateTimeField()
    Arrival_date_time = models.DateTimeField()
    price = models.CharField(max_length=128)
    journey_type = models.CharField(max_length=128, default='One Way')

    def __str__(self):
        """
        :return: a description of Journey Object
        """
        return self.flight_code

    def list_cities_journeys(self, airports_list, departure_date, journey_type):
        """
        :param airports_list:
        :param departure_date:
        :param journey_type:
        :return: A list of Journeys from city to city in this date
        """
        list_of_journeys = Journey.objects.filter(origin_airport__in=list(airports_list[0]),
                                                  arrival_airport__in=list(airports_list[1]),
                                                  Departure_date_time__startswith=departure_date.date(),
                                                  journey_type=journey_type).values()
        return list(list_of_journeys)

    def list_airports_journeys(self, airports_list, departure_date, journey_type):
        """
        :param airports_list:
        :param departure_date:
        :param journey_type:
        :return: A list of Journeys from one airport to other in this date
        """
        list_of_journeys = Journey.objects.filter(origin_airport=Airport.objects.get(airport_name=airports_list[0]),
                                                  arrival_airport=
                                                  Airport.objects.get(airport_name=airports_list[1]),
                                                  Departure_date_time__startswith=departure_date.date(),
                                                  journey_type= journey_type).values()
        return list(list_of_journeys)

    def list_city_airport_journey(self, airports_list, flying_to_airport, departure_date, journey_type):
        """
        :param airports_list:
        :param flying_to_airport:
        :param departure_date:
        :param journey_type:
        :return: A list of Journeys from one city to airport in this date
        """
        list_of_journeys = Journey.objects.filter(origin_airport__in=list(airports_list[0]),
                                                  arrival_airport= Airport.objects.get(airport_name=flying_to_airport),
                                                  Departure_date_time__startswith=departure_date.date(),
                                                  journey_type=journey_type).values()
        return list(list_of_journeys)

    def list_airport_city_journey(self, flying_from_airport, airports_list, departure_date, journey_type):
        """
        :param flying_from_airport:
        :param airports_list:
        :param departure_date:
        :param journey_type:
        :return: A list of Journeys from one airport to city in this date
        """
        list_of_journeys = Journey.objects.filter(origin_airport=Airport.objects.get(airport_name=flying_from_airport),
                                                  arrival_airport__in= list(airports_list[0]),
                                                  Departure_date_time__startswith=departure_date.date(),
                                                  journey_type=journey_type).values()
        return list(list_of_journeys)

