__author__ = 'Kunya'
import json
from Flight import Flight

class FlightParser:

    def __init__(self, jsonFlights):
        self.data = jsonFlights# json.loads(jsonFlights)
        self.carriers = self.parseCarriers()
        self.flights = self.createFlights()
        for f in self.flights:
            print (f)


    def parseCarriers(self):
        ret = {}
        carriers = self.data['trips']['data']['carrier']
        for carrier in carriers:
            ret[carrier['code']] = carrier['name']
        return ret



    def createFlights(self):
        allOptions = self.data['trips']['tripOption']
        flights = []
        for option in allOptions:
            price  = option['saleTotal']
            for slice in option['slice']:
                for segment in slice['segment']:
                    airline = self.carriers.get( segment['flight']['carrier'], segment['flight']['carrier'])
                    leg = segment['leg'][0]
                    arrivalTime = leg['arrivalTime']
                    depTime = leg['departureTime']
                    dest = leg['destination']
                    origin = leg['origin']
                    meal = leg['meal']
                    f= Flight(depTime, arrivalTime, origin, dest, price , airline, meal)
                    flights.append(f)
        return flights





#with open('C:\Users\Kunya\Desktop\jsonFlights.txt') as json_data:
#    d = json.load(json_data)
#    f = FlightParser(d)
#    print(d)