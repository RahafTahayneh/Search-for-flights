from django.db import models
from nltk import python_2_unicode_compatible
from .city import City


@python_2_unicode_compatible
class Airport(models.Model):
    airport_id = models.IntegerField(primary_key=True)
    airport_name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    def __str__(self):
        return self.airport_name

    def check_if_exist(self, airport):
        """
        :param airport:
        :return: True, if airport entered by User is exist in database, False if not
        """
        airport = Airport.objects().get(airport_name=airport).count()
        if airport > 0:
            return True
        return False







