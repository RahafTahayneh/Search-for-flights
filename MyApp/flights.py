from MyApp.models import City, Journey, Airport

cities = []
airports = []
flights = []
is_from_city = False
is_to_city = False


class Flights:

    def __init__(self, flying_from, flying_to, departure_date=None, journey_type=None):
        self.flying_from = flying_from
        self.flying_to = flying_to
        self.departure_date= departure_date
        self.journey_type = journey_type

    def check_distinations(self):
        if City().check_if_exist(self.flying_from):
            global is_from_city
            is_from_city = True
        if City().check_if_exist(self.flying_to):
            global is_to_city
            is_to_city = True

    def choose_distenation(self):
        if is_from_city and is_to_city:
            return self.city_city()
        elif not is_from_city and not is_to_city :
            self.airport_airport()
        elif is_from_city and not is_to_city :
            self.city_airport()
        elif not is_from_city and is_to_city :
            self.airport_city()

    def city_city(self):
        global airports,flights
        airports = City().list_cities_airports(self.flying_from, self.flying_to)
        flights = Journey().list_cities_journeys(airports,self.departure_date, self.journey_type)
        return list(flights)

    def airport_airport(self):
        global airports, flights
        airports = [self.flying_from, self.flying_to]
        flights = Journey().list_airports_journeys(airports, self.departure_date, self.journey_type)
        return list(flights)

    def city_airport(self):
        global airports, flights
        airports = City().list_city_airports(self.flying_from)
        flights = Journey().list_city_airport_journey(airports, self.flying_to, self.departure_date,  self.journey_type)
        return list(flights)

    def airport_city(self):
        global airports, flights
        airports = City().list_city_airports(self.flying_to)
        flights = Journey().list_airport_city_journey(self.flying_from, airports, self.departure_date,  self.journey_type)
        return list(flights)























