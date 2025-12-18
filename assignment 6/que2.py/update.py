import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)
sensor_id = int(input("Enter Sensor ID: "))
new_moisture = float(input("Enter new moisture level: "))

query = "UPDATE soil_moisture SET moisture_level=%s WHERE sensor_id=%s"
cursor = conn.cursor()
cursor.execute(query, (new_moisture, sensor_id))
conn.commit()

print("Record Updated Successfully")


cursor.close()
conn.close()