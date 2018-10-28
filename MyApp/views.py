from datetime import datetime
from django.http import JsonResponse
from MyApp.flights import Flights

journeys_list = {}


def get_flight_request(request):
    """
    :param request:
    :return: Json response contains list of journeys based on user request
    """
    global journeys_list
    flying_from = request.GET.get('flying_from')
    flying_to = request.GET.get('flying_to')
    departure_date = request.GET.get('departuring_date')
    datetime_filter_departure = convert_to_date_format(departure_date)

    if request.GET.get('returning_date'):
        flight = Flights(flying_from, flying_to, datetime_filter_departure, 'Roundtrip')
        flight.check_distinations()
        journeys_list = flight.choose_distenation()
        return JsonResponse(journeys_list, safe=False)

    else:
        flight = Flights(flying_from, flying_to, datetime_filter_departure, 'One Way')
        flight.check_distinations()
        journeys_list = flight.choose_distenation()
        return JsonResponse(journeys_list, safe=False)


def convert_to_date_format(departure_date):
    departure_date = departure_date.split("-")
    datetime_filter = datetime(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
    return datetime_filter
