__author__ = 'Kunya'
import urllib2
import json
from datetime import timedelta, date


url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyD393u1O37d-NHhJqdiJ-yZBK_vgRSWfIc"
import copy


def getSliceForDay(day, ori, dest):
    return {
        "maxStops": 0,
        "origin": ori,
        "destination": dest,
        "date": day.isoformat()
      }

REQUEST = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": 2,
    },
  #  "slice": [
  #    {
  #      "maxStops": 0,
  #      "origin": "TLV",
  #      "destination": "NYC",
  #      "date": "2017-11-20",
  #    },
  #    {
  #      "maxStops": 0,
  #      "origin": "TLV",
  #      "destination": "NYC",
  #      "date": "2017-11-21",
  #    }
  #  ],
    "refundable": "false",
    #"solutions": 5
  }
}

def getAllFlights(airport, startDate, endDate):
    toRequest = copy.deepcopy(REQUEST)
    slices = []
    d = startDate
    delta = timedelta(days=1)
    while d <= endDate:
        slices.append(getSliceForDay(d, 'TLV', airport))
        d += delta
    toRequest['request']['slice'] = slices

    response = sendRequest( toRequest )
    return response


def sendRequest(request):
    jsonreq = json.dumps(request, encoding = 'utf-8')
    req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
    flight = urllib2.urlopen(req)
    response = flight.read()
    json1_data = json.loads(response)
    return json1_data
