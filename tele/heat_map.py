import csv
import folium
from folium.plugins import HeatMap

# filename = '/home/clover/catkin_ws/Code/tele/telemetry.csv'
filename = '/home/clover/catkin_ws/Code/tele/telemetry2.csv'

latitude_values = []
longitude_values = []

# Открытие csv в режиме для чтения
with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')

    # Чтение заголовков
    headers = next(csv_reader)
    print("Заголовки",headers)

    # Чтение данных построчно
    for row in csv_reader:
        if row:
            latitude_values.append(float(row[1]))
            longitude_values.append(float(row[2]))

center_lat = sum(latitude_values) / len(latitude_values)
center_lon = sum(longitude_values) / len(longitude_values)

m = folium.Map(location=[center_lat, center_lon], zoom_start=18)

heat_data = []

for i in range(len(latitude_values)):
    lat = latitude_values[i]
    lon = longitude_values[i]
    coordinates = [lat, lon]

    heat_data.append(coordinates)

    HeatMap(heat_data).add_to(m)

m.save("heatmap.html")