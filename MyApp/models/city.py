from django.db import models
from nltk import python_2_unicode_compatible


@python_2_unicode_compatible
class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=128)

    def __str__(self):
        return self.city_name

    def list_city_airports(self,flying_city):
        cities_ls = City.objects.prefetch_related('airports')
        airports = []
        for city in cities_ls:
            if city.city_name == flying_city:
                airports.append(
                    city.airports.values_list('airport_id', flat=True))
        return airports

    def list_cities_airports(self, flying_from, flying_to):
        cities_ls = City.objects.prefetch_related('airports')
        airports = []
        for city in cities_ls:
            if city.city_name == flying_from or city.city_name == flying_to:
                airports.append(
                                city.airports.values_list('airport_id', flat= True))
        return airports

    def check_if_exist(self, city):
        """

        :param city:
        :return: True, if city entered by User is exist in database, False if not
        """
        city = City.objects.filter(city_name=city).count()
        if city > 0:
            return True
        return False








