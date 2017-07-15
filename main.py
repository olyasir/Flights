__author__ = 'Kunya'
import json
from datetime import timedelta, date
from googApi import getAllFlights
from fParser import FlightParser

CITY_TO_CODE_MAP = {'Berlin':'BER', 'Amsterdam':'AMS', 'Paris':'CDG', 'Frankfurt':'FRA', 'Rome':'FCO',
                    'Milan': 'MXP', 'Moscow':'MOW', 'Madrid':'MAD', 'Warsaw':'WAW'  }

def getAllEvents(city):
    #call api to get all concerts
    #sort concerts by date
    return []


def run():
    for city, airport in CITY_TO_CODE_MAP.iteritems():
        allEvent = getAllEvents(city)
        if not allEvent:
            continue
        startDate = min(date.todate(),  allEvent[0].date - timedelta(3))
        endDate = allEvent[-1].date + timedelta(3)

        allFlightsJson  = getAllFlights(airport, startDate, endDate)
        p = FlightParser(allFlightsJson)
        for i in p.flights:
            print(i)




allFlightsJson = getAllFlights('BER', date.today()+timedelta(1), date.today()+timedelta(2))
p = FlightParser(allFlightsJson)
for i in p.flights:
    print(i)