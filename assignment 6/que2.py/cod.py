import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)

cursor = conn.cursor()

query = "SELECT * FROM soil_moisture WHERE moisture_level < 35"
cursor.execute(query)
records = cursor.fetchall()

print("All Records:")
for row in records:
    print(row)

cursor.close()
conn.close()
