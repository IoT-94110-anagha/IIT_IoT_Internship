import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)



id_value = int(input("Enter ID: "))

query=f"delete from  sensor_readings where id='{id_value}';"

cursor=conn.cursor()
cursor.execute(query)
conn.commit()
print("record deleted ")
cursor.close()
conn.close()