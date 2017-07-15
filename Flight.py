__author__ = 'Kunya'

class Flight:

    def __init__(self, departureTime, arrivalTime, fromCity, toCity, price , airline, meal):
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.fromCity = fromCity
        self.toCity = toCity
        self.price = price
        self.airline = airline
        self.meal = meal

    def __str__(self):
        ret =    "{}: {}({})--->{}({}) {}".format(self.airline, self.fromCity, self.departureTime, self.toCity, self.arrivalTime, self.price)
        return ret






