import csv
import matplotlib.pyplot as plt

filename = '/home/clover/catkin_ws/Code/tele/telemetry.csv'

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

# Построение графика
plt.figure(figsize=(15,7))
plt.plot(time_values, altitude_values, label = "Time/Altitude", color = 'blue')
plt.xlabel('Time')
plt.ylabel('Altitude (m)')
plt.title('Drone Altitude Over Time')
plt.legend()
plt.grid()
plt.savefig("Time_Alt.png")
plt.show()
