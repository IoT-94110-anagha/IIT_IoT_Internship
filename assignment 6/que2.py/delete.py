import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)
sensor_id = int(input("Enter Sensor ID: "))
query = "DELETE FROM soil_moisture WHERE sensor_id=%s"
cursor=conn.cursor()
cursor.execute(query, (sensor_id,))

conn.commit()

print("Record Updated Successfully")


cursor.close()
conn.close()