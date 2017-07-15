__author__ = 'Kunya'
import os
import sqlite3

DB_FILE_NAME = 'flights.db'
SCHEMA_FILE_NAME = 'flights_schema.sql'

class FlightsDB:
    def __init__(self):
        db_is_new = not os.path.exists(DB_FILE_NAME)
        with sqlite3.connect(DB_FILE_NAME) as conn:
            if db_is_new:
                print ('Creating schema')
                with open(SCHEMA_FILE_NAME, 'rt') as f:
                    schema = f.read()
                    conn.executescript(schema)

    def addFlight(self, date, source, dest, price, airline, timestamp, json):
        with sqlite3.connect(DB_FILE_NAME) as conn:
            conn.execute("""
            insert into Flights (fdate, source, dest, price, airline, ftimestamp, json)
            values ( '{}', '{}', '{}', '{}', '{}', '{}', '{}') """.format(date, source, dest, price, airline,timestamp, json)
            )
            conn.commit()

    def getFlights(self, source, dest, startDate, endDate):
        query = """select fdate, source, dest, price, airline, ftimestamp from Flights where
         source = '{}'
         and dest = '{}'
         and fdate >= '{}'
         and fdate <= '{}'
         order by fdate""".format(source, dest, startDate, endDate)
        with sqlite3.connect(DB_FILE_NAME) as conn:
            # Change the row factory to use Row
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query)
            return [row for row in cursor.fetchall()]



from datetime import datetime
db = FlightsDB()
#db.addFlight(datetime(2017,1,1), 'TLV', 'BER', '654USD', 'El Al', datetime.today(), '{some jsom: kjheedh}')

print (db.getFlights('TLV', 'BER', datetime(2017,1,1), datetime(2017,1,1)))