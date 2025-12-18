import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cursor = conn.cursor()

id_value = int(input("Enter ID: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))


insert_query = """
INSERT INTO sensor_readings (id, temperature, humidity, timestamp)
VALUES (%s, %s, %s, %s)
"""


cursor.execute(insert_query, (id_value, temperature, humidity, datetime.now()))
conn.commit()

print("Record inserted successfully")


cursor.close()
conn.close()
