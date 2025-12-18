import requests
import sqlite3
import time
"""
----------------------------------------------------------------------
ISS Tracker Pipeline
----------------------------------------------------------------------
Description: 
    Real-time ETL pipeline that extracts ISS telemetry data from 
    OpenNotify and loads it into a local SQLite database for
    historical tracking.
    
Usage: 
    Run this script in the background to build the dataset.
----------------------------------------------------------------------
"""
DB_name = 'iss.db'
API_URL = "http://api.open-notify.org/iss-now.json"

connection = sqlite3.connect("iss.db")
cursor = connection.cursor()
sql_command = """
CREATE TABLE IF NOT EXISTS iss_history (
    latitude TEXT, 
    longitude TEXT
);
"""
cursor.execute(sql_command)
connection.commit()
print(f"Database Connected: {DB_name}")

print(f"---STARTING ISS TRACKER---")
while True:
    try:
        #extract: fetching raw JSON from API
        response = requests.get(API_URL)
        data = response.json()

        #transform: specific coordinates
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']

        print(f"Current location of ISS: {lat},{lon}")

        #Load: inserting record into warehouse
        insert_sql = "INSERT INTO iss_history (latitude, longitude) VALUES (?, ?)"
        cursor.execute(insert_sql, (lat, lon))
        connection.commit()
        print("Saved to DB")
    except Exception as e:
        #log errors without crashing the pipeline
        print(f"Error Occurred: {e}")
    #rate limiting
    time.sleep(5)

