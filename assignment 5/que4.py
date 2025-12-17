import datetime
current_datetime = datetime.datetime.now()
print("current date and time =",current_datetime)
day_name = current_datetime.strftime("%A")
print("Day of the Week:", day_name)