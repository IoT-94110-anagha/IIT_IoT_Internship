import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture "
)

cursor = conn.cursor()

sensor_id = int(input("Enter Sensor ID: "))
moisture = float(input("Enter Moisture Level: "))
dt = datetime.now()

query = "INSERT INTO soil_moisture VALUES (%s, %s, %s)"
cursor.execute(query, (sensor_id, moisture, dt))
conn.commit()

print("Record Inserted Successfully")

cursor.close()
conn.close()
