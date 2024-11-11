import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = '/home/clover/catkin_ws/Code/tele/telemetry.csv'
filename = '/home/clover/catkin_ws/Code/tele/telemetry2.csv'
time_values = []
altitude_values = []

# Открытие csv в режиме для чтения
with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Чтение заголовков
    headers = next(csv_reader)
    print("Заголовки",headers)

    # Чтение данных построчно
    for row in csv_reader:
        if row:
            time_values.append(row[0])
            altitude_values.append(float(row[6]))

min_altitude = min(altitude_values)
max_altitude = max(altitude_values)
min_index = altitude_values.index(min_altitude)
max_index = altitude_values.index(max_altitude)

# Построение графика
plt.figure(figsize=(15,7))
plt.plot(time_values, altitude_values, label = "Time/Altitude", color = 'blue')
plt.scatter(time_values, altitude_values, color="green")
plt.scatter(time_values[max_index],max_altitude, color='red', label = "Max Altitude")
plt.scatter(time_values[min_index],min_altitude, color="purple", label = "Min Altitude")
plt.xlabel('Time')
plt.ylabel('Altitude (m)')
plt.title('Drone Altitude Over Time')
plt.legend()
plt.grid()
plt.savefig("Time_Alt3.png")
plt.show()
