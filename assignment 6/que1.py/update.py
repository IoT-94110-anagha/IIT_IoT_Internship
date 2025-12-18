import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)



id_value = int(input("Enter ID: "))
temperature = float(input("Enter Temperature: "))

query=f"update sensor_readings SET temperature='{temperature}'where id='{id_value}';"

cursor=conn.cursor()
cursor.execute(query)
conn.commit()
print("record updated ")
cursor.close()
conn.close()