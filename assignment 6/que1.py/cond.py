import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cursor = conn.cursor()
query = """select*from sensor_readings where temperature  between 11 and 27"""
cursor.execute(query)
sensor_readings=cursor.fetchall()
for sensor_readings in sensor_readings:
    print(sensor_readings)

cursor.close()
conn.close()
