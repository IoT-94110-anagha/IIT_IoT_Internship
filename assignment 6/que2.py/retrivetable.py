import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM soil_moisture")
records = cursor.fetchall()

print("All Records:")
for row in records:
    print(row)

cursor.close()
conn.close()
